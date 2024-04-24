import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("facebook.csv")
data.head()

print("Mean: ",data.mean(numeric_only=True))
print("Median: ",data.median(numeric_only=True))
print("Mode: ",data.mode(numeric_only=True))

print("Max: ",data.max(numeric_only=True))
print("Min: ",data.min(numeric_only=True))

print("Variance: ",data.var(numeric_only=True))
print("Standard deviation: ",data.std(numeric_only=True))
print("Skewness: ",data.skew(numeric_only=True))
print("Kurtosis: ",data.kurt(numeric_only=True))

sns.boxplot(x = 'age', data = data)
plt.title("Boxplot")
plt.show()

plt.hist(x = 'age', data = data)
plt.title("Histogram")
plt.show()

plt.bar(data['age'], data['tenure'])
plt.title("Bar")
plt.show()

plt.figure(figsize=(17,6))
sns.lineplot(x = data['age'], y = data['tenure'])
plt.show()

plt.figure(figsize=(17,6))
sns.scatterplot(x = data['age'], y = data['tenure'])
plt.show()