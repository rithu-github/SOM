# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from minisom import MiniSom

# Load dataset
dataset = pd.read_csv('annex1.csv')  # Replace with your dataset path
X = dataset.iloc[:, :-1].values  # Assuming last column is the label

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Assuming 'customer_data.csv' is loaded with some non-numeric data
dataset = pd.read_csv('annex1.csv')

# Encode categorical columns (example: 'Customer' and 'Category')
for column in dataset.columns:
    if dataset[column].dtype == 'object':  # Check for non-numeric columns
        encoder = LabelEncoder()
        dataset[column] = encoder.fit_transform(dataset[column])

# After encoding, separate the features
X = dataset.iloc[:, :-1].values  # Assuming the last column is the label

# Feature scaling (only after encoding categorical data)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)



# Initialize the SOM
som = MiniSom(x=10, y=10, input_len=X.shape[1], sigma=1.0, learning_rate=0.5)

# Train the SOM
som.random_weights_init(X_scaled)
som.train_random(X_scaled, num_iteration=100)

# Plotting the SOM
plt.figure(figsize=(10, 10))
plt.pcolor(som.distance_map().T, cmap='coolwarm')  # Distance map as a heatmap
plt.colorbar()

# Add markers for winning nodes
for i, x in enumerate(X_scaled):
    winning_node = som.winner(x)
    plt.text(winning_node[0] + 0.5, 
             winning_node[1] + 0.5, 
             dataset.iloc[i, -1],  # Plot customer label if available
             ha='center', va='center')

plt.title('Customer Segmentation with SOM')
plt.show()
