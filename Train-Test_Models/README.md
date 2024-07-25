# Train-Test Models

For training and testing the models first we have to create the dataset. To create the dataset please refer to [Dataset_Creation](https://github.com/eniac00/ProteoKnight/tree/main/Dataset_Creation). 

After creating the dataset copy the dataset (i.e.  binary_dataset or mutli_dataset) to this folder `Train-Test_Models`.

```shell
cd Train-Test_Models
```

```shell
cp -r ../Dataset_Creation/binary_dataset/* ./datasets/
```

Like, [Dataset_Creation](https://github.com/eniac00/ProteoKnight/tree/main/Dataset_Creation) again create a virtual environment and install the dependencies using the `requirements.txt`

## Train-Test

To train and test the models we can use the the below `notebook` files,

* `googlenet_binary.ipynb`
* `googlenet_multi.ipynb`

For evaluation these `notebook` can be used,

* `evaluation_binary.ipynb`
* `evaluation_multi.ipynb`

The already trained models (i.e. the `*.pth`) are,

* `googlenet_binary_89.pth`
* `googlenet_mutli_77.pth`

The below listed files are individual modules and will be used to facilitate the training and testing process,

* `data_setup.py`

* `engine.py`

* `utils.py`

## Models

These models were also used while conducting the research and have been mentioned in the paper.

* Efficientnet_v2_small
* GoogLeNet
* CCT_7
* MobileNet_v3_small

# Note

In the shared `notebook` file we have only shown the `googlenet` model from `torchvision`. The other models those have been mentioned in the paper can also be implemented using the `notebooks`. For more information regarding the models please refer to [Torchvision Models](https://pytorch.org/vision/stable/models.html) and [Compact Transformers](https://github.com/SHI-Labs/Compact-Transformers).

  

  



