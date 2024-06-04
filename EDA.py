import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("data/data.csv")

# Overview of the dataset
num_rows, num_cols = data.shape
data_types = data.dtypes

print("Number of rows:", num_rows)
print("Number of columns:", num_cols)
print("\nData types:")
print(data_types)

# Summary statistics
summary_stats = data.describe()
print("\nSummary Statistics:")
print(summary_stats)

# Distribution of Numerical Features
numerical_features = data.select_dtypes(include=[float, int]).columns

for feature in numerical_features:
    plt.figure(figsize=(8, 6))
    data[feature].hist(bins=20)
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.title("Distribution of " + feature)
    plt.show()