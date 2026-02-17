# ============= even_loop_while.py =============
def even_loop_while():
    i = 2
    while i <= 100:
        print(i)
        i += 2


# ============= even_loop.py =============
def even_loop():
    # Print even numbers up to 100 (2..100)
    for i in range(2, 101, 2):
        print(i)


# ============= multiplication_table_while.py =============
def multiplication_table_while():
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            print(f"{i}x{j}={i*j}", end="\t")
            j += 1
        print()
        i += 1


# ============= multiplication_table.py =============
def multiplication_table():
    # Print a 10x10 multiplication table using nested for-loops
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i}x{j}={i*j}", end="\t")
        print()


# ============= odd_numbers_while.py =============
def odd_numbers_while():
    i = 1
    while i < 100:
        print(i)
        i += 2


# ============= odd_numbers.py =============
def odd_numbers():
    # Print odd numbers up to 100 (1..99)
    for i in range(1, 100, 2):
        print(i)


# ============= sum_even_while.py =============
def sum_even_while():
    upto = 100
    total = 0
    i = 2
    while i <= upto:
        total += i
        i += 2
    print(f"Sum of even numbers from 1 to {upto} is {total}")


# ============= sum_even.py =============
def sum_evens(upto=100):
    return sum(i for i in range(2, upto + 1, 2))


def sum_even():
    upto = 100
    total = sum_evens(upto)
    print(f"Sum of even numbers from 1 to {upto} is {total}")


# ============= sum_odd_while.py =============
def sum_odd_while():
    upto = 100
    total = 0
    i = 1
    while i <= upto:
        total += i
        i += 2
    print(f"Sum of odd numbers from 1 to {upto} is {total}")


# ============= sum_odd.py =============
def sum_odds(upto=100):
    return sum(i for i in range(1, upto + 1, 2))


def sum_odd():
    upto = 100
    total = sum_odds(upto)
    print(f"Sum of odd numbers from 1 to {upto} is {total}")


# ============= table_and_pattern_reversed_while.py =============
def print_table_reversed_while(n=5, upto=10):
    i = upto
    while i >= 1:
        print(f"{i}x{n}={i * n}")
        i -= 1


def print_triangle_reversed_while(rows=5):
    i = rows
    while i >= 1:
        print('*' * i)
        i -= 1


# ============= table_and_pattern_reversed.py =============
def print_table_reversed(n=5, upto=10):
    for i in range(upto, 0, -1):
        print(f"{i}x{n}={i * n}")


def print_triangle_reversed(rows=5):
    for i in range(rows, 0, -1):
        print('*' * i)


# ============= table_and_pattern_while.py =============
def print_table_while(n=5, upto=10):
    i = 1
    while i <= upto:
        print(f"{i}x{n}={i * n}")
        i += 1


def print_triangle_while(rows=5):
    i = 1
    while i <= rows:
        print('*' * i)
        i += 1


# ============= table_and_pattern.py =============
def print_table(n=5, upto=10):
    for i in range(1, upto + 1):
        print(f"{i}x{n}={i * n}")


def print_triangle(rows=5):
    for i in range(1, rows + 1):
        print('*' * i)


if __name__ == "__main__":
    print("=== FOR LOOPS ===\n")
    
    print("--- Even Loop ---")
    even_loop()
    
    print("\n--- Multiplication Table ---")
    multiplication_table()
    
    print("\n--- Odd Numbers ---")
    odd_numbers()
    
    print("\n--- Sum Even ---")
    sum_even()
    
    print("\n--- Sum Odd ---")
    sum_odd()
    
    print("\n--- Table and Pattern ---")
    print_table()
    print()
    print_triangle()
    
    print("\n--- Table and Pattern Reversed ---")
    print_table_reversed()
    print()
    print_triangle_reversed()
    
    print("\n\n=== WHILE LOOPS ===\n")
    
    print("--- Even Loop While ---")
    even_loop_while()
    
    print("\n--- Multiplication Table While ---")
    multiplication_table_while()
    
    print("\n--- Odd Numbers While ---")
    odd_numbers_while()
    
    print("\n--- Sum Even While ---")
    sum_even_while()
    
    print("\n--- Sum Odd While ---")
    sum_odd_while()
    
    print("\n--- Table and Pattern While ---")
    print_table_while()
    print()
    print_triangle_while()
    
    print("\n--- Table and Pattern Reversed While ---")
    print_table_reversed_while()
    print()
    print_triangle_reversed_while()
