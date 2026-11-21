import pandas as pd

features = pd.read_csv("features.csv", sep=";")
patient_info = pd.read_csv("patient_info.csv", sep=";")

print(features.shape)
print(features.columns[:20])
print(patient_info.columns)

data = features.merge(patient_info, on="ID", how="inner")
