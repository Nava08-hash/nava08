#!/usr/bin/env python3

def sum_odds(upto=100):
    return sum(i for i in range(1, upto + 1, 2))


def main():
    upto = 100
    total = sum_odds(upto)
    print(f"Sum of odd numbers from 1 to {upto} is {total}")


if __name__ == "__main__":
    main()
