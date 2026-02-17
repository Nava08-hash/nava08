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


if __name__ == "__main__":
    run_examples()