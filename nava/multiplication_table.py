#!/usr/bin/env python3

def main():
    # Print a 10x10 multiplication table using nested for-loops
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i}x{j}={i*j}", end="\t")
        print()


if __name__ == "__main__":
    main()
