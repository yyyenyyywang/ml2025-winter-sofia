from module5_mod import NumberFinder

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
