# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset
data = pd.read_csv('C:\\Users\\Akshaya\\OneDrive\\Documents\\Module16\\Titanic Dataset.csv')
print(data.head(5))

print("\nData Types:\n")
print(data.dtypes)

# Check Null Values
print("\nNull Values:\n")
print(data.isnull().sum())
