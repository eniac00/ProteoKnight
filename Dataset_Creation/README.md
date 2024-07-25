# ProteoKnight
intro will go here



Clone the whole repository using `git` command or download the zip file and extract.

```shell
git clone https://github.com/KennthShang/PhaVIP.git
```

# Creating the Dataset

To create the image dataset from the text dataset, it would be best if we create a python environment and install the dependencies there.

## Virtual Environment

We are first creating a virtual environment name `proteo`.

```shell
python -m venv proteo
```

Activate the virtual environment.

```shell
source ./proteo/bin/activate
```

## Install the dependencies

```shell
pip install -r requirements.txt
```

## Build the Dataset

After successfully installing all the depencies just fire the below command to create the dataset (by default it is `binary class`).

```shell
python DatasetBuilder.py
```

If you wish to make the `multi class` dataset you can change the `root = './multi_datasets'` along with the defined dictionary in the `./SequenceEncoder/DatasetBuilder.py` like below and again fire the above command.

```python
if __name__=="__main__":
    root = './multi_datasets'
    family_path = {
            'baseplate': '../fasta_datasets/Multi/baseplate.fasta',
            'major_capsid': '../fasta_datasets/Multi/major_capsid.fasta',
            'major_tail': '../fasta_datasets/Multi/major_tail.fasta',
            'minor_capsid': '../fasta_datasets/Multi/minor_capsid.fasta',
            'minor_tail': '../fasta_datasets/Multi/minor_tail.fasta',
            'other': '../fasta_datasets/Multi/other.fasta',
            'portal': '../fasta_datasets/Multi/portal.fasta',
            'tail_fiber': '../fasta_datasets/Multi/tail_fiber.fasta',
            }

    DatasetBuilder(root, family_path, max_workers=5).run()
```

After the successful execution you will see a folder in the parent directory, whatever you set in the `root` variable (e.g. binary_datasets or mutli_datasets).
