import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def read_dataset(num_points, dataset_name=""):
    print(f"Enter {num_points} (x, y) pairs for {dataset_name} set:")
    x_list = [0.0] * num_points
    y_list = [0] * num_points
    for i in range(num_points):
        while True:
            try:
                x_val = float(input(f"Enter x value for dataset#{i+1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a real number for x.")
        while True:
            try:
                y_val = input(f"Enter y value for dataset#{i+1}: ")
                y_int = int(y_val)
                if y_int < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a non-negative integer for y.")
        x_list[i] = x_val
        y_list[i] = y_int
    return np.array(x_list).reshape(-1, 1), np.array(y_list)

def main():
    # Read the training data
    N = int(input("Enter the number of training data points (N): "))
    X_train, y_train = read_dataset(N, "training")

    # Read the testing data
    M = int(input("Enter the number of test data points (M): "))
    X_test, y_test = read_dataset(M, "test")

    # hyperparameter search
    param_grid = {'n_neighbors': list(range(1, 11))}
    knn = KNeighborsClassifier()
    grid_search = GridSearchCV(knn, param_grid, cv=3)

    grid_search.fit(X_train, y_train)
    best_k = grid_search.best_params_['n_neighbors']
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Best k: {best_k}")
    print(f"Test Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()
