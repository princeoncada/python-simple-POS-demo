import os
from datetime import datetime

# Global variables
gates_inventory = []
order = {}


def save_inventory():
    with open("inventory.txt", "w") as file:
        for gate in gates_inventory:
            file.write(f"{gate['name']}\n")
            file.write(f"{gate['price']}\n")
            file.write(f"{gate['quantity']}\n")
            file.write("\n")


def print_receipt(payment):
    with open("receipt.txt", "w") as file:
        total = 0
        print("\n" + "-" * 40)
        file.write("-" * 40 + "\n")

        print("Prince Smart Gates".center(40))
        file.write("Prince Smart Gates".center(40) + "\n")

        print("-" * 40)
        file.write("-" * 40 + "\n")

        print("This is the Official Receipt:".center(40))
        file.write("Receipt:".center(40) + "\n")

        print("-" * 40)
        file.write("-" * 40 + "\n")

        for product, value in order.items():
            print(f'{product}'.ljust(20) + f'${value["price"]:.2f}'.rjust(10))
            file.write(f'{product}'.ljust(20) + f'${value["price"]:.2f}'.rjust(10) + "\n")

            print(f'Quantity: {value["quantity"]}'.ljust(20))
            file.write(f'Quantity: {value["quantity"]}'.ljust(20) + "\n")

            print(f'-' * 40)
            file.write(f'-' * 40 + "\n")

        for product in order:
            total += order[product]["price"] * order[product]["quantity"]

        print(f'Total: ${total:.2f}'.rjust(30))
        file.write(f'Total: ${total:.2f}'.rjust(30) + "\n")

        print(f'Payment: ${payment:.2f}'.rjust(30))
        file.write(f'Payment: ${payment:.2f}'.rjust(30) + "\n")

        print(f'Change: ${payment - total:.2f}'.rjust(30))
        file.write(f'Change: ${payment - total:.2f}'.rjust(30) + "\n")

        print("-" * 40)
        file.write("-" * 40 + "\n")

        print("Thank you for shopping!".center(40))
        file.write("Thank you for shopping!".center(40) + "\n")

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Date and Time: {current_datetime}".center(40))
        file.write(f"Date and Time: {current_datetime}".center(40) + "\n")

        print("-" * 40)
        file.write("-" * 40 + "\n")


def print_item(items):
    print("-" * 30)
    for item, item_data in items.items():
        print(f"{item}".ljust(20) + f"${item_data['price']:.2f}".rjust(10))
        print(f"Quantity: {item_data['quantity']}".ljust(20))
        print("-" * 30)


def leave():
    save_inventory()
    print("Thank you for shopping with us today!")
    print("Goodbye!")


def checkout():
    total = 0
    for fruit in order:
        total += order[fruit]["price"] * order[fruit]["quantity"]
    print("")
    print(f"Your order:")
    print_item(order)

    print(f"Your total is ${total:.2f}")
    while True:
        payment = float(input("Enter your payment: "))
        if payment < total:
            print("Insufficient funds!")
        else:
            break
    change = payment - total
    print(f"Total cost: ${total:.2f}")
    print(f"Payment: ${payment:.2f}")
    print(f"Change: ${change:.2f}")
    print_receipt(payment)
    leave()


def choose(choice):
    choice -= 1
    if choice == 5:
        checkout()
        return
    if choice == 6:
        leave()
        return

    print(f"Selected: {gates_inventory[choice]['name']}")
    if gates_inventory[choice]["quantity"] == 0:
        print("Sorry, we are out of stock for this item.")
        print("")
        print("")
        display_menu()
        return

    while True:
        quantity = input("How many would you like? ")
        if quantity.isdigit() and 0 < int(quantity) <= gates_inventory[choice]["quantity"]:
            quantity = int(quantity)
            break
        else:
            print("Invalid input!")

    if gates_inventory[choice]["name"] in order:
        order[gates_inventory[choice]["name"]]["quantity"] += quantity
        gates_inventory[choice]["quantity"] -= quantity
    else:
        order[gates_inventory[choice]["name"]] = {
            "quantity": quantity,
            "price": gates_inventory[choice]["price"]
        }
        gates_inventory[choice]["quantity"] -= quantity
    print(f"{quantity} {gates_inventory[choice]['name']} added to cart.")
    print("")
    display_menu()


def load_inventory():
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        for i in range(0, len(lines), 4):
            gates_inventory.append({
                "name": lines[i],
                "price": float(lines[i + 1]),
                "quantity": int(lines[i + 2])
            })


def display_menu():
    print("Menu:")
    for i, fruit_obj in enumerate(gates_inventory):
        print(f"{i + 1}. {fruit_obj['name']}: ${fruit_obj['price']:.2f} per unit")
    print("6: Checkout")
    print("7: Exit")
    choose(int(input("Enter your choice: ")))


def main():
    load_inventory()
    print("Welcome to the Pre-Order Gates Store!")
    display_menu()


if __name__ == "__main__":
    main()
