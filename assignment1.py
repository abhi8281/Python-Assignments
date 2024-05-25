def triangle(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")

        # Print asterisks for the current row
        for k in range(1, 2 * i):
            print("*", end="")

        # Move to the next line after printing each row
        print()


def main():
    n = int(input("Enter the number of rows for the triangle: "))
    triangle(n)


if __name__ == "__main__":
    main()
