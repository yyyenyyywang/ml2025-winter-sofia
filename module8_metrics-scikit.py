import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    while True:
        try:
            N = int(input("Enter the number of data points: "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
    
    true_array = np.zeros(N, dtype=int)
    predicted_array = np.zeros(N, dtype=int)
    
    print("\nEnter N (x, y) points (one by one) where x is ground-truth (0/1) and y is predicted (0/1):")
    for i in range(N):
        while True:
            try:
                x = int(input(f"Point {i+1} - Enter ground truth x (0 or 1): "))
                if x not in [0, 1]:
                    raise ValueError
                y = int(input(f"Point {i+1} - Enter predicted y (0 or 1): "))
                if y not in [0, 1]:
                    raise ValueError
                true_array[i] = x
                predicted_array[i] = y
                break
            except ValueError:
                print("Invalid input. Please enter only 0 or 1.")
    
    precision = precision_score(true_array, predicted_array, zero_division=0)
    recall = recall_score(true_array, predicted_array, zero_division=0)
    
    print("\nResults:")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")

if __name__ == "__main__":
    main()
