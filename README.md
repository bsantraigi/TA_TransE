# Code framework for Temporal KG completion.

Implementation of Temporal Knowledge Graph Completion following the work of Duran et al., [Learning Sequence Encoders for Temporal Knowledge Graph Completion](https://arxiv.org/abs/1809.03202)

- Code:
    - modify based on [knowledge_representation_pytorch](https://github.com/jimmywangheng/knowledge_representation_pytorch)
    - 1st column in train.txt - subject entity
    - 2nd column - relation
    - 3rd column - object entity
    - 4th column - time

    - 1st figure in stat.txt - number of entities
    - 2nd figure in stat.txt - number of relations
    
    used `preprocess_TA_step1.py` and `preprocess_TA_step2.py` to make data for TA_TransE.
    ```
    python preprocess_TA_step1.py ICEWS14
    python preprocess_TA_step2.py ICEWS14
    ```
    Note : data is already Preprocessed.
    if you have new data then you can follow the above Process i.e. "python preprocess_TA_step1.py ICEWS14"



- TATransE.py : train code

- You can run the code with 
	```
	python TA_TransE.py ICEWS14
	
	```
	eg:
	```
	cd ./baselines
	CUDA_VISIBLE_DEVICES=0 python TA_TransE.py -f 1 -d ICEWS14 -L 1 -bs 1024 -n 1000

	```
Note: when you run the code like python "TA_TransE.py ICEWS14",
you need to give dataset in argument with out _TA


