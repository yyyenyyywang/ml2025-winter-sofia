import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    N = int(input("Enter number (N): "))
    k = int(input("Enter number (k): "))

    if k > N:
        print("Error: k cannot be greater than N.")
        return

    x_list = []
    y_list = []
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        x_list.append([x])  
        y_list.append(y)

    X_train = np.array(x_list)
    y_train = np.array(y_list)

    variance = np.var(y_train)
    print(f"Variance of training labels: {variance:.4f}")

    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    X_input = float(input("Enter X value to predict Y: "))
    X_test = np.array([[X_input]])

    y_pred = model.predict(X_test)
    print(f"Predicted Y value: {y_pred[0]:.4f}")

if __name__ == "__main__":
    main()
