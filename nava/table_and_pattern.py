#!/usr/bin/env python3

def print_table(n=5, upto=10):
    for i in range(1, upto + 1):
        print(f"{i}x{n}={i * n}")


def print_triangle(rows=5):
    for i in range(1, rows + 1):
        print('*' * i)


def main():
    print_table()
    print()
    print_triangle()


if __name__ == "__main__":
    main()
