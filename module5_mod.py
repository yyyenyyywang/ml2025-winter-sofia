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