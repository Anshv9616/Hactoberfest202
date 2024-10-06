""" This program calculates the factorial of a number using different methods. """

def factorial(n):
    """ This function calculates the factorial of a number using an iterative approach. """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):  # Start from 2 to avoid unnecessary multiplications
        result *= i
    return result

def factorial_while(n):
    """ This function calculates the factorial of a number using a while loop. """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def main():
    """ The main function to demonstrate the factorial calculations. """
    test_value = 5
    print(f"factorial({test_value}) = {factorial(test_value)}")
    print(f"factorial_while({test_value}) = {factorial_while(test_value)}")

if __name__ == "__main__":
    main()
