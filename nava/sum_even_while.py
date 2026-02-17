#!/usr/bin/env python3

def main():
    upto = 100
    total = 0
    i = 2
    while i <= upto:
        total += i
        i += 2
    print(f"Sum of even numbers from 1 to {upto} is {total}")

if __name__ == "__main__":
    main()
