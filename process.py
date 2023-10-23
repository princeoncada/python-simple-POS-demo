from inventory import save_inventory, load_inventory
from print import print_menu, print_item, print_receipt

gates_inventory = []
order = {}


def leave():
    save_inventory(gates_inventory)
    print("Thank you for shopping with us today!")
    print("Goodbye!")


def checkout():
    total = 0
    payment = 0
    for fruit in order:
        total += order[fruit]["price"] * order[fruit]["quantity"]
    print("")
    print(f"Your order:")
    print_item(order)

    print(f"Your total is ${total:.2f}")

    while True:
        print("")
        try:
            payment = float(input("Enter payment amount | 0 > back: "))
            if payment == 0:
                print("")
                print_menu(gates_inventory, choose)
                return
            if payment < total:
                print("Insufficient payment! Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please try again.")
            continue

    change = payment - total
    print(f"Total cost: ${total:.2f}")
    print(f"Payment: ${payment:.2f}")
    print(f"Change: ${change:.2f}")
    print_receipt(payment, order)
    leave()


def choose(choice):
    choice -= 1
    if choice == 5:
        if len(order.keys()) == 0:
            print("You have not ordered anything!")
            print("")
            print_menu(gates_inventory, choose)
            return
        checkout()
        return
    if choice == 6:
        leave()
        return

    print(f"Selected: {gates_inventory[choice]['name']}")
    print("")
    if gates_inventory[choice]["quantity"] == 0:
        print("Sorry, we are out of stock for this item.")
        print("")
        print("")
        print_menu(gates_inventory, choose)
        return

    while True:
        quantity = input("How many would you like? | 0 > cancel: ")
        if quantity == "0":
            print("")
            print_menu(gates_inventory, choose)
            return

        if quantity.isdigit() and 0 < int(quantity) <= gates_inventory[choice]["quantity"]:
            quantity = int(quantity)
            break
        else:
            print("Invalid input! Please try again.")
            print("")
            continue

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
    print_menu(gates_inventory, choose)


def main():
    global gates_inventory
    gates_inventory = load_inventory(gates_inventory)
    print("Welcome to the Pre-Order Gates Store!")
    print_menu(gates_inventory, choose)
