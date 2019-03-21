# Database based cache to dope the result retrieval from reaction rules

Thomas Duigou (thomas.duigou@inra.fr), INRA, 2019

Here it is a two components cache system:

- A python module to be used with ...
- A Mongo database, which should be started independently (see "How to run the database in the background")

Notice : at reading time, some of following information might be deprecated!

## Needed components

- docker
- docker-compose
- conda

## Setting up python environment

Basically: one needs a conda environment with following packages:
- rdkit
- pymongo
- pytest

```
conda create --name myenv python=3.6
source activate myenv
conda install --channel rdkit rdkit=2018.09.1.0
conda install --channel conda-forge pytest
conda install pytest
conda install pymongo
conda install yaml
```

## Install as a packages

```
pip install -e .
```


## How to run the database in the background
 
 ```
 docker-compose -f service/run/mongo.yml
 ```
 
## Q&A

- Where are stored the db files ? In a named docker data volume `mongo-data`.
