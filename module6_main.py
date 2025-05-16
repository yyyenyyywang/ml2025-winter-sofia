from knn import KNNRegressor

N = int(input("Enter total number of data (N): "))
k = int(input("Enter total number of neighbors (k): "))

x_points = []
y_points = []

for i in range(N):
    x = float(input(f"Enter x value for data {i+1}: "))
    y = float(input(f"Enter y value for data {i+1}: "))
    x_points.append(x)
    y_points.append(y)

regressor = KNNRegressor(k)
regressor.insert_data(x_points, y_points)

x_input = float(input("Enter the X value to predict Y: "))

try:
    prediction = regressor.predict(x_input)
    print(f"Predicted Y value: {prediction}")
except ValueError as e:
    print(f"Found an error: {e}")
