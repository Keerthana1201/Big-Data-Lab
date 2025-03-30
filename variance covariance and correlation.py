import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
data = load_iris()
df = pd.DataFrame(data=data.data, columns=data.feature_names)
correlation_matrix = df.corr()
covariance_matrix = df.cov()
variance = df.var()
correlation_matrix.to_csv('iris_correlation.csv', index=True)
covariance_matrix.to_csv('iris_covariance.csv', index=True)
variance.to_csv('iris_variance.csv', index=True)
print("Correlation Matrix:")
print(correlation_matrix)
print("\nCovariance Matrix:")
print(covariance_matrix)
print("\nVariance of each feature:")
print(variance)
print("\nFiles saved successfully")