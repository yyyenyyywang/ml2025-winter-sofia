import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.x = None
        self.y = None

    def insert_data(self, x_points, y_points):
        self.x = np.array(x_points)
        self.y = np.array(y_points)

    def predict(self, X_input):
        if self.x is None or self.y is None:
            raise ValueError("x or y cannot be an empty array.")
        if self.k > len(self.x):
            raise ValueError("k cannot be greater than the number of data points.")

        # Compute Euclidean distances
        distances = np.abs(self.x - X_input)
        indices = np.argsort(distances)[:self.k]
        return np.mean(self.y[indices])
