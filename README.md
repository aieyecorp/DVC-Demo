# DVC-Demo

## Intialize dvc in github
```dvc init```

## To track data version, add  data.csv file in dvc
```dvc add data/data.csv```

## To track data version in github, add and commit data/data.csv.dvc 
```git add data/data.csv.dvc```

## To store data in remote storage, create remode connection
```dvc remote add -d <remote_storage_name> <location>```

