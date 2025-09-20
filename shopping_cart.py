# shopping_cart.py
# CSE 110 - W05 Shopping Cart Project
# Starter code

cart = []
prices = []

def show_menu():
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def add_item():
    item = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    cart.append(item)
    prices.append(price)
    print(f'"{item}" has been added to the cart.')

def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("\n--- Your Cart ---")
        for i, (item, price) in enumerate(zip(cart, prices), start=1):
            print(f"{i}. {item} - ${price:.2f}")

def remove_item():
    view_cart()
    if cart:
        choice = int(input("Enter the item number to remove: "))
        if 1 <= choice <= len(cart):
            removed = cart.pop(choice-1)
            prices.pop(choice-1)
            print(f'"{removed}" has been removed.')
        else:
            print("Invalid selection.")

def compute_total():
    total = sum(prices)
    print(f"\nTotal amount: ${total:.2f}")

# Main program loop
while True:
    show_menu()
    option = input("Choose an option: ")
    if option == "1":
        add_item()
    elif option == "2":
        view_cart()
    elif option == "3":
        remove_item()
    elif option == "4":
        compute_total()
    elif option == "5":
        print("Thank you for using the shopping cart. Goodbye! and have a nice day!")
        break
    else:
        print("Invalid choice. Try again.")
