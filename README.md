## Diploma

### KAGGLE TO KEEL

Converts a particular dataset .csv format .dat

```
1 python -m pip install -r requeriments.txt
2 kaggle-to-keel.py
```

### Cross validation partition

cvpartition(n,'KFold',k) returns a cvpartition object that defines a random nonstratified partition for k-fold cross-validation on n observations. The partition randomly divides the observations into k disjoint subsamples, or folds, each of which has approximately the same number of observations.

Creates a random 10-fold partition.
```
fold=cvpartition(10, 'kfold', kfold);
```