N = int(input("Enter a positive integer N: "))

# Read N numbers one by one and store them in a list
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

X = int(input("Enter the number X to search for: "))

if X in numbers:
    index = numbers.index(X) + 1  # Convert to 1-based index
    print(index)
else:
    print("-1")