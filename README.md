# DVC-Demo

## Intialize dvc in github
```dvc init```

## To track data version, add  data.csv file in dvc
```dvc add data/data.csv```

## To track data version in github, add and commit data/data.csv.dvc 
```git add data/data.csv.dvc```

## To store data in remote storage, create remode connection
```dvc remote add -d <remote_storage_name> <location>```

## To intgrate pipeline reproducibilty, we will create dvc.yaml and we will use `dvc repro` command.
Assume in our demo we have 3 stages:
1. In stage_01, we are doing write operation for 2 files `artifacts.txt` and `artifacts_2.txt`
2. In stage_02, we are reading file `artifacts.txt`
3. In stage_03, we are reading file `artifacts_2.txt`

### dvc.yaml format for above pipeline:
```
stages:
        stage_01:
                cmd: python stage_01.py
                deps:
                        - stage_01.py
                outs:
                        - artifacts.txt
                        - artifacts_2.txt

        stage_02:
                cmd: python stage_02.py
                deps:
                        - stage_02.py
                        - artifacts.txt
        stage_03:
                cmd: python stage_03.py
                deps:
                        - stage_03.py
                        - artifacts_2.txt
```

Pipeline has following direct acyclic graph:
```

            +----------+             
            | stage_01 |             
            +----------+             
           ***         ***           
          *               *          
        **                 **        
+----------+            +----------+ 
| stage_02 |            | stage_03 | 
+----------+            +----------+ 
+-------------------+  
| data/data.csv.dvc |  
+-------------------+  

```

