import pandas as pd

features = pd.read_csv("features.csv", sep=";")
patient_info = pd.read_csv("patient_info.csv", sep=";")

print(features.shape)
print(features.columns[:20])
print(patient_info.columns)

data = features.merge(patient_info, on="ID", how="inner")

selected_features = [
    "ID",
    "ACC__mean",
    "ACC__standard_deviation",
    "ACC__root_mean_square",
    "ACC__maximum",
    "ACC__mean_abs_change",
    "ACC__sample_entropy"
]
