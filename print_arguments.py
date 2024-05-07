#!/usr/bin/python3
import sys

def main():
    # Check if there are arguments other than the script name
    if len(sys.argv) > 1:
        # Iterate through the arguments starting from index 1 (skipping script name)
        for i in range(1, len(sys.argv)):
            print(sys.argv[i])
    else:
        print("No arguments provided.")

if __name__ == "__main__":
    main()
