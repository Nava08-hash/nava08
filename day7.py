"""
==============================================
        PIZZA BILL GENERATOR
==============================================
"""

def display_pizzas():
    """Display available pizza options"""
    print("\n" + "="*50)
    print("               PIZZA MENU")
    print("="*50)
    print("\n1. Normal Veg Pizza           - ₹300")
    print("2. Normal Non-Veg Pizza      - ₹400")
    print("3. Delux Veg Pizza           - ₹600")
    print("4. Delux Non-Veg Pizza       - ₹800")
    print("="*50)


def display_addons():
    """Display available add-ons"""
    print("\n" + "="*50)
    print("               ADD-ONS MENU")
    print("="*50)
    print("\n1. Extra Cheese              - ₹100")
    print("2. Extra Topping             - ₹100")
    print("3. Take Away Bag Charges     - ₹20")
    print("4. Water Bottle              - ₹20")
    print("5. Ketchup (each)            - ₹5")
    print("6. Soft Drinks (each)        - ₹75")
    print("="*50)


def get_pizza():
    """Get pizza selection from user"""
    pizzas = {
        1: ("Normal Veg Pizza", 300),
        2: ("Normal Non-Veg Pizza", 400),
        3: ("Delux Veg Pizza", 600),
        4: ("Delux Non-Veg Pizza", 800)
    }
    
    while True:
        display_pizzas()
        try:
            choice = int(input("\nEnter pizza choice (1-4): "))
            if choice in pizzas:
                name, price = pizzas[choice]
                return name, price
            else:
                print("❌ Invalid choice! Please select 1-4")
        except ValueError:
            print("❌ Please enter a valid number!")


def get_addons():
    """Get add-ons selection from user"""
    addons_list = {
        1: ("Extra Cheese", 100, 1),
        2: ("Extra Topping", 100, 1),
        3: ("Take Away Bag Charges", 20, 1),
        4: ("Water Bottle", 20, 1),
        5: ("Ketchup", 5, None),  # None means quantity is needed
        6: ("Soft Drinks", 75, None)  # None means quantity is needed
    }
    
    selected_addons = []
    total_addons = 0
    
    while True:
        display_addons()
        print("\nEnter addon number to add (or 0 to finish):")
        
        try:
            choice = int(input("\nEnter addon choice (1-6, or 0 to finish): "))
            
            if choice == 0:
                break
            
            if choice in addons_list:
                name, price, default_qty = addons_list[choice]
                
                # For items like ketchup and soft drinks, ask for quantity
                if default_qty is None:
                    while True:
                        try:
                            qty = int(input(f"How many {name}? "))
                            if qty <= 0:
                                print("❌ Please enter a positive number!")
                                continue
                            addon_cost = price * qty
                            selected_addons.append((name, qty, price, addon_cost))
                            total_addons += addon_cost
                            print(f"✓ Added: {qty} {name}(s) - ₹{addon_cost}")
                            break
                        except ValueError:
                            print("❌ Please enter a valid number!")
                else:
                    addon_cost = price * default_qty
                    selected_addons.append((name, default_qty, price, addon_cost))
                    total_addons += addon_cost
                    print(f"✓ Added: {name} - ₹{addon_cost}")
            else:
                print("❌ Invalid choice! Please select 1-6")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    return selected_addons, total_addons


def generate_bill(pizza_name, pizza_price, addons, addon_total):
    """Generate and display the bill"""
    subtotal = pizza_price + addon_total
    tax = round(subtotal * 0.05, 2)  # 5% tax
    total = subtotal + tax
    
    print("\n" + "="*50)
    print("               BILL DETAILS")
    print("="*50)
    print(f"\n{'Item':<30} {'Qty':<8} {'Price':>10}")
    print("-"*50)
    
    # Pizza
    print(f"{pizza_name:<30} {'1':<8} ₹{pizza_price:>8}")
    
    # Add-ons
    if addons:
        print("\nAdd-Ons:")
        for name, qty, price, total_addon_price in addons:
            if qty == 1:
                print(f"  {name:<26} {'1':<8} ₹{total_addon_price:>8}")
            else:
                print(f"  {name:<26} {qty:<8} ₹{total_addon_price:>8}")
    
    print("\n" + "-"*50)
    print(f"{'Subtotal':<40} ₹{subtotal:>8.2f}")
    print(f"{'Tax (5%)':<40} ₹{tax:>8.2f}")
    print("-"*50)
    print(f"{'TOTAL AMOUNT':<40} ₹{total:>8.2f}")
    print("="*50)
    print("\nThank you for your order! 🍕")
    print("="*50 + "\n")


def main():
    """Main function to run pizza bill generator"""
    print("\n" + "="*50)
    print("    WELCOME TO PIZZA BILL GENERATOR")
    print("="*50)
    
    # Get pizza selection
    pizza_name, pizza_price = get_pizza()
    print(f"\n✓ Selected: {pizza_name} - ₹{pizza_price}")
    
    # Get add-ons
    addons, addon_total = get_addons()
    
    # Generate bill
    generate_bill(pizza_name, pizza_price, addons, addon_total)
    
    # Ask if user wants to order again
    while True:
        again = input("Do you want to place another order? (yes/no): ").lower().strip()
        if again in ['yes', 'y']:
            main()
            break
        elif again in ['no', 'n']:
            print("\n" + "="*50)
            print("         Visit Again! Goodbye! 👋")
            print("="*50 + "\n")
            break
        else:
            print("❌ Please enter 'yes' or 'no'")


if __name__ == "__main__":
    main() 

# stack=[]

# while True:
#     print("n1. Push 2. Pop 3. Display 4. Exit")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         val=int(input("enter value"))
#         stack.appdend()(val)
#     elif choice==2:
#         if not stack:
#             print("stack is empty")
#         else:
#             print("popped value is",stack.pop())
#     elif choice==3:
#         if not stack:
#             print("stack is empty")
#         else:
#             print("top")
#     elif choice==4: 
#         print("stack",stack)
#     else:        
#         print("invalid choice")
         