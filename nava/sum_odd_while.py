#!/usr/bin/env python3

def main():
    upto = 100
    total = 0
    i = 1
    while i <= upto:
        total += i
        i += 2
    print(f"Sum of odd numbers from 1 to {upto} is {total}")

if __name__ == "__main__":
    main()
