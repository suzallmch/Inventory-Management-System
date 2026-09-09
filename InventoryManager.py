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


