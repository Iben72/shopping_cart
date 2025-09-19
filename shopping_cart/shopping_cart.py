#create codes for a shopping cart, by asking the user to add an item,stating the name of the item, price of the item, quantity to buy
# display items in the cart, remove items, total cost of the items and mode of payment
# which could be by cheque, cash or bank transfer.

# Simple Shopping Cart Program

cart = []

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Checkout")
    print("5. Stop Shopping")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter item name: ")
        try:
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            cart.append({"name": name, "price": price, "quantity": quantity})
            print(f"{quantity} x {name} added to cart.")
        except ValueError:
            print("❌ Invalid input. Please enter numbers for price and quantity.")

    elif choice == "2":
        if not cart:
            print("\n🛒 Your cart is empty.\n")
        else:
            print("\n🛒 Items in your cart:")
            for i, item in enumerate(cart, start=1):
                print(f"{i}. {item['name']} - ${item['price']} x {item['quantity']} = ${item['price'] * item['quantity']}")

    elif choice == "3":
        if not cart:
            print("\n🛒 Your cart is empty.\n")
        else:
            print("\n🛒 Items in your cart:")
            for i, item in enumerate(cart, start=1):
                print(f"{i}. {item['name']} - ${item['price']} x {item['quantity']} = ${item['price'] * item['quantity']}")
            try:
                remove_index = int(input("Enter item number to remove: ")) - 1
                if 0 <= remove_index < len(cart):
                    removed = cart.pop(remove_index)
                    print(f"❌ Removed {removed['name']} from cart.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("❌ Please enter a valid number.")

    elif choice == "4":
        if not cart:
            print("\n🛒 Your cart is empty.\n")
        else:
            total = sum(item['price'] * item['quantity'] for item in cart)
            print("\n🛒 Items in your cart:")
            for i, item in enumerate(cart, start=1):
                print(f"{i}. {item['name']} - ${item['price']} x {item['quantity']} = ${item['price'] * item['quantity']}")
            print(f"\n💰 Total Cost: ${total:.2f}")

            print("\nPayment Methods: cheque / cash / bank transfer")
            payment = input("Choose mode of payment: ").strip().lower()
            if payment in ["cheque", "cash", "bank transfer"]:
                print(f"✅ Payment of ${total:.2f} made via {payment}. Thank you for shopping!")
                break
            else:
                print("❌ Invalid payment method. Try again.")

    elif choice == "5":
        print("🛑 Shopping stopped. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")


