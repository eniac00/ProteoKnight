#!/usr/bin/env python3

from SequenceEncoder import SequenceEncoder
from tqdm.contrib.concurrent import thread_map
from sklearn.model_selection import train_test_split
import pandas as pd
import os
import time
from Bio import SeqIO
from pathlib import Path
from functools import partial
import shutil


class DatasetBuilder:
    def __init__(self, root=None, family_path=None, max_workers=10, limit=False, limit_size=500):
        if root and family_path:
            self.root = root
            self.family_path = family_path
            self.paths_list = ['train', 'test']
            self.families = list(self.family_path.keys())
            self.max_workers = max_workers
            self.limit=limit
            self.limit_size=limit_size
            self.tw = shutil.get_terminal_size()[0]

            self.createDirStructure()
        else:
            print("Error")

    def run(self):
        for family, path in self.family_path.items():
            print(f"\n\n\n{'='*self.tw}")
            print(f"{family.center(len(family)+2, ' '):$^{self.tw}}")
            df = self.fastaToDataFrame(path)
            self.createImages(df, family)
            print(f"{family.rjust(len(family)+1, ' ') + 'Done'.center(6, ' '):$^{self.tw}}")
            print(f"{'='*self.tw}\n\n\n")


    def createDirStructure(self):
        print(f"{'Folder Creation'.center(17, ' '):#^{self.tw}}")
        root = Path(self.root)
        for path in self.paths_list:
            for family in self.families:
                full_path = root / path / family
                if not os.path.exists(full_path):
                    os.makedirs(full_path)
                    print(f"{full_path} has been created")
                else:
                    print(f"{full_path} already exists, Skipping")
        print(f"{'Folder Creation Done'.center(22, ' '):#^{self.tw}}")


    def fastaToDataFrame(self, path):
        print(f"{'Fasta To DataFrame'.center(20, ' '):#^{self.tw}}\n")
        name = []
        sequence = []
        for record in SeqIO.parse(path, 'fasta'):
            name.append(record.name)
            sequence.append(str(record.seq))

        if self.limit:
            name = name[:self.limit_size]
            sequence = sequence[:self.limit_size]

        name_series = pd.Series(name)
        sequence_series = pd.Series(sequence)

        df = pd.DataFrame({'name': name_series, 'sequence': sequence_series})
        print(f"Successfully parsed {path}")
        print(f"\n{'Fasta To DataFrame Finished'.center(29, ' '):#^{self.tw}}")

        return df


    def encoder(self, row, path, family):
        SequenceEncoder(seq=row[2]).save(f"{self.root}/{path}/{family}/{row[1]}")


    def createImages(self, df, family):
        print(f"\n{'Train Test Split'.center(18, ' '):#^{self.tw}}\n")
        train, test = train_test_split(df, test_size=0.3)
        print("Successfully splited the Dataframe")
        print(f"\n{'Train Test Split Done'.center(23, ' '):#^{self.tw}}\n")

        print(f"\n{' Converting train' + family.center(len(family)+2, ' '):#^{self.tw}}\n")
        thread_map(partial(self.encoder, path='train', family=family), train.itertuples(), max_workers=self.max_workers, total=train.shape[0])
        print(f"\n{' Converting train ' + family + 'Done'.center(6, ' '):#^{self.tw}}\n")

        print(f"\n{' Converting test' + family.center(len(family)+2, ' '):#^{self.tw}}\n")
        thread_map(partial(self.encoder, path='test', family=family), test.itertuples(), max_workers=self.max_workers, total=test.shape[0])
        print(f"\n{' Converting test ' + family + 'Done'.center(6, ' '):#^{self.tw}}")





if __name__=="__main__":
    root = './binary_datasets'
    family_path = {
            'PVP': '../fasta_datasets/Binary/pvp.fa',
            'non-PVP': '../fasta_datasets/Binary/non_pvp.fa'
            }

    DatasetBuilder(root, family_path, max_workers=5).run()


