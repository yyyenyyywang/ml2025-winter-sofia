class NumberFinder:
    def __init__(self):
        self.numbers = []

    def insert_numbers(self, n):
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            self.numbers.append(num)

    def search_number(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1  # start from 1
        else:
            return -1

def main():
    finder = NumberFinder()

    # Input N
    N = int(input("Enter a positive integer N: "))

    # Read N 
    finder.insert_numbers(N)

    # Search X
    X = int(input("Enter the number X to search for: "))
    result = finder.search_number(X)

    # Output result
    print(result)

if __name__ == "__main__":
    main()
