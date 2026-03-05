# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries Imported\n")

# Import dataset
data = pd.read_csv(r'C:\Users\Akshaya\OneDrive\Documents\Module16\IMDB Dataset.csv')

print("Dataset Loaded Successfully\n")

# Show first 5 rows
print("First 5 Rows:\n")
print(data.head(5))

# Check Null Values
print("\nNull Values:\n")
print(data.isnull().sum())

# Plot Histogram for Runtime
plt.figure()
plt.hist(data['Runtime'])
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.title("Runtime Distribution")
plt.show()

# Plot Histogram for IMDB Rating
plt.figure()
plt.hist(data['IMDB_Rating'])
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.title("IMDB Rating Distribution")
plt.show()

# Define bins for Runtime
bins_time = np.arange(80, 230, 10)

plt.figure()
plt.hist(data['Runtime'], edgecolor="black", bins=bins_time,color='g')
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.title("Runtime Distribution (With Bins)")
plt.show()

# Define bins for Rating
bins_rating = np.arange(8, 10, 0.20)

plt.figure()
plt.hist(data['IMDB_Rating'], edgecolor="black", bins=bins_rating,color='g')
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.title("IMDB Rating Distribution (With Bins)")
plt.xticks(bins_rating)
plt.show()