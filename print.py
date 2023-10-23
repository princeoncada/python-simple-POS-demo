from datetime import datetime


def print_receipt(payment, order):
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


def print_menu(gates_inventory, choose):
    print("Menu:")
    for i, fruit_obj in enumerate(gates_inventory):
        print(f"{i + 1}. {fruit_obj['name']}: ${fruit_obj['price']:.2f} per unit")
    print("6: Checkout")
    print("7: Exit")

    while True:
        try:
            choice = input("Enter your choice: ")
            choose(int(choice))
            break
        except ValueError:
            print(f"Invalid input! Please try again.")
            print("")
            continue
