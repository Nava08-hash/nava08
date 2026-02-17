#!/usr/bin/env python3

def print_table(n=5, upto=10):
    i = 1
    while i <= upto:
        print(f"{i}x{n}={i * n}")
        i += 1


def print_triangle(rows=5):
    i = 1
    while i <= rows:
        print('*' * i)
        i += 1


def main():
    print_table()
    print()
    print_triangle()


if __name__ == "__main__":
    main()
