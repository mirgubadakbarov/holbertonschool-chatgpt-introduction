#!/usr/bin/python3
import sys

def factorial(n):
    """Calculates the factorial of a non-negative integer n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    """Main function to calculate factorial from command-line input."""
    # Ensure there is exactly one command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <non-negative integer>")
        sys.exit(1)
    
    try:
        # Convert argument to integer
        number = int(sys.argv[1])
        
        # Ensure the number is non-negative
        if number < 0:
            print("Error: Please enter a non-negative integer.")
            sys.exit(1)
        
        # Calculate factorial and print the result
        f = factorial(number)
        print(f)
    
    except ValueError:
        # Handle invalid integer input
        print("Error: Please enter a valid integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()
