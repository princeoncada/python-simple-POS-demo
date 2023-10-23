def save_inventory(gates_inventory):
    with open("inventory.txt", "w") as file:
        for gate in gates_inventory:
            file.write(f"{gate['name']}\n")
            file.write(f"{gate['price']}\n")
            file.write(f"{gate['quantity']}\n")
            file.write("\n")


def load_inventory(gates_inventory):
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        for i in range(0, len(lines), 4):
            gates_inventory.append({
                "name": lines[i],
                "price": float(lines[i + 1]),
                "quantity": int(lines[i + 2])
            })
    return gates_inventory
