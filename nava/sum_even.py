#!/usr/bin/env python3

def sum_evens(upto=100):
    return sum(i for i in range(2, upto + 1, 2))


def main():
    upto = 100
    total = sum_evens(upto)
    print(f"Sum of even numbers from 1 to {upto} is {total}")


if __name__ == "__main__":
    main()
