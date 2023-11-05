import datasets
import pandas as pd
from csvHandling import dataFrame1

dataDict = dataFrame1.to_dict(orient="list")

hugFaceDataSet = datasets.Dataset.from_dict(dataDict)

hugFaceDataSet.save_to_disk("hugFaceData")

print(hugFaceDataSet)
