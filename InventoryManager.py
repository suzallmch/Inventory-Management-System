# inventory holds all items
# each item name points to another dictionary with price and quantity
inventory = {
    "pen": {"price": 10, "quantity": 5},
    "notebook": {"price": 50, "quantity": 20},
    "eraser": {"price": 5, "quantity": 30},
    "sharpener": {"price": 8, "quantity": 15}
}


def add_item(name, price, quantity):
    # creates a new key in inventory with the given price and quantity
    inventory[name] = {"price": price, "quantity": quantity}
    print(name, "added!")


def view_inventory():
    # loop through every item and print its details
    for name, details in inventory.items():
        print(name, "-> price: $" + str(details["price"]), ", qty:", details["quantity"])


def update_quantity(name, new_quantity):
    # only update if the item actually exists
    if name in inventory:
        inventory[name]["quantity"] = new_quantity
        print(name, "quantity updated to", new_quantity)
    else:
        print(name, "not found in inventory.")


def remove_item(name):
    # only remove if the item actually exists
    if name in inventory:
        del inventory[name]
        print(name, "removed!")
    else:
        print(name, "not found in inventory.")


def search_item(name):
    # only show details if the item actually exists
    if name in inventory:
        details = inventory[name]
        print(name, "-> price: $" + str(details["price"]), ", qty:", details["quantity"])
    else:
        print(name, "not found in inventory.")


def check_low_stock(threshold):
    # loop through inventory and print items below the threshold
    print(f"\n--- Low Stock Items (below {threshold}) ---")
    found = False
    for name, details in inventory.items():
        if details["quantity"] < threshold:
            print(name, "-> qty:", details["quantity"])
            found = True
    if not found:
        print("No items are low on stock.")


def sell_item(name, qty_sold):
    # only sell if the item exists
    if name not in inventory:
        print(name, "not found in inventory.")
        return

    # only sell if there's enough stock
    if qty_sold > inventory[name]["quantity"]:
        print("Not enough stock. Only", inventory[name]["quantity"], "left.")
        return

    # deduct stock and calculate total
    inventory[name]["quantity"] -= qty_sold
    total = inventory[name]["price"] * qty_sold
    print(f"Sold {qty_sold} {name}(s) for ${total}. Remaining stock: {inventory[name]['quantity']}")


# menu loop
while True:
    print("\n1. Add  2. View  3. Update  4. Remove  5. Search  6. Low Stock  7. Sell  8. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        add_item(name, price, qty)
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        name = input("Name: ")
        qty = int(input("New quantity: "))
        update_quantity(name, qty)
    elif choice == "4":
        name = input("Name: ")
        remove_item(name)
    elif choice == "5":
        name = input("Name: ")
        search_item(name)
    elif choice == "6":
        threshold = int(input("Low stock threshold: "))
        check_low_stock(threshold)
    elif choice == "7":
        name = input("Name: ")
        qty = int(input("Quantity sold: "))
        sell_item(name, qty)
    elif choice == "8":
        break
    else:
        print("Invalid choice.")