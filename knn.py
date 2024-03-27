import numpy as np

# Function to compute Euclidean distance
def distance(x, X):
    return np.sqrt(np.sum((x-X)**2))

# Function to perform KNN
def KNN(X, Y, x, K=5):
    m = X.shape[0]
    x = x.flatten()
    val = []
    for i in range(m):
        xi = X[i]
        dist = distance(x, xi)
        val.append((dist, Y[i]))
    val = sorted(val, key=lambda x: x[0])[:K]
    val = np.array(val)
    # Count the frequency of each class in the K neighbors
    labels = val[:, 1]
    unique_labels, counts = np.unique(labels, return_counts=True)
    # Find the label with the most count
    index = counts.argmax()
    prediction = unique_labels[index]
    return prediction