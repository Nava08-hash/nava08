# ============= demo.py =============
def calculate_ticket(age: int, show_time: str, senior_discount_pct: float = 0.20, morning_discount: float = 50.0):
	"""Decide ticket category, base price, discounts and final price.

	Rules implemented:
	  - age < 5: free entry
	  - 5 <= age <= 17: child ticket (₹150)
	  - 18 <= age <= 59: adult ticket (₹250)
	  - age >= 60: senior ticket (₹200) with senior discount (default 20%)
	  - show_time: 'morning' gets additional ₹50 off (if not free); 'evening' no time discount

	Returns a dict with keys: eligible, category, base_price, discount, final_price, message
	"""
	if age < 0:
		return {
			'eligible': False,
			'category': None,
			'base_price': 0.0,
			'discount': 0.0,
			'final_price': 0.0,
			'message': 'Invalid age',
		}

	show = show_time.strip().lower()
	if show not in ('morning', 'evening'):
		return {
			'eligible': False,
			'category': None,
			'base_price': 0.0,
			'discount': 0.0,
			'final_price': 0.0,
			'message': 'Unknown show time',
		}

	# Determine category and base price
	if age < 5:
		category = 'Free (toddler)'
		base = 0.0
		discount = 0.0
		final = 0.0
		message = 'Free entry for children under 5'
		return {
			'eligible': True,
			'category': category,
			'base_price': base,
			'discount': discount,
			'final_price': final,
			'message': message,
		}
	elif 5 <= age <= 17:
		category = 'Child'
		base = 150.0
	elif 18 <= age <= 59:
		category = 'Adult'
		base = 250.0
	else:
		category = 'Senior'
		base = 200.0

	discount = 0.0
	# Apply senior discount (percentage off base)
	if category == 'Senior':
		discount += base * senior_discount_pct

	# Apply show time discount (flat ₹50 for morning shows)
	if show == 'morning' and base > 0:
		discount += morning_discount

	final_price = max(0.0, base - discount)
	message = f"{category} ticket: base ₹{base}, discount ₹{discount:.2f}, final ₹{final_price:.2f}"

	return {
		'eligible': True,
		'category': category,
		'base_price': base,
		'discount': discount,
		'final_price': final_price,
		'message': message,
	}


def run_examples():
	examples = [
		# (age, show_time)
		(3, 'morning'),    # free
		(10, 'evening'),   # child, no morning discount
		(30, 'morning'),   # adult, morning discount ₹50
		(65, 'evening'),   # senior, senior discount applied
		(70, 'morning'),   # senior + morning discount
	]

	for age, show in examples:
		result = calculate_ticket(age, show)
		print(f"Age: {age}, Show: {show}")
		print(f"  {result['message']}")
		print()


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


# ============= ticket_cli.py =============
import sys


def main():
    # Accept optional CLI args: age show_time
    if len(sys.argv) >= 3:
        try:
            age = int(sys.argv[1])
        except ValueError:
            print("Invalid age provided")
            return
        show = sys.argv[2]
    else:
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Invalid age input")
            return
        show = input("Enter show time (morning/evening): ")

    result = calculate_ticket(age, show)
    if not result.get('eligible'):
        print(result.get('message'))
        return

    print(result.get('message'))


def run_all_while_loops():
	"""Run all while loop demonstrations"""
	print("===== EVEN LOOP WHILE =====")
	even_loop_while()
	
	print("\n===== MULTIPLICATION TABLE WHILE =====")
	multiplication_table_while()
	
	print("\n===== ODD NUMBERS WHILE =====")
	odd_numbers_while()
	
	print("\n===== SUM EVEN WHILE =====")
	sum_even_while()
	
	print("\n===== SUM ODD WHILE =====")
	sum_odd_while()
	
	print("\n===== TABLE AND PATTERN WHILE =====")
	print_table_while()
	print()
	print_triangle_while()
	
	print("\n===== TABLE AND PATTERN REVERSED WHILE =====")
	print_table_reversed_while()
	print()
	print_triangle_reversed_while()


if __name__ == '__main__':
    main()
