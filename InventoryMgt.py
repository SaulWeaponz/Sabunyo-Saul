def display_inventory(inventory):
    """Displays the current inventory."""
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_inventory(inventory):
    """Updates the inventory based on user input."""
    item = input("Enter item name to update (or 'done' to finish): ").lower()
    if item == "done":
        return
    elif item in inventory:
          while True:
            try:
                quantity_change = int(input(f"Enter quantity to add or subtract (e.g., +5, -3) for {item}: "))
                inventory[item] += quantity_change
                print(f"{item} updated. New quantity: {inventory[item]}")
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter an integer.")
    else:
        print(f"{item} not found in inventory.")

def add_new_item(inventory):
    """Adds a new item to the inventory."""
    item = input("Enter new item name: ").lower()
    if item not in inventory:
        while True:
            try:
                quantity = int(input(f"Enter initial quantity for {item}: "))
                inventory[item] = quantity
                print(f"{item} added to inventory.")
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter an integer.")
    else:
        print(f"{item} already exists in inventory.")

# Initial inventory
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 25,
}

while True:
    print("\nOptions:")
    print("1. Display Inventory")
    print("2. Update Inventory")
    print("3. Add New Item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_inventory(inventory)
    elif choice == "2":
        update_inventory(inventory)
    elif choice == "3":
        add_new_item(inventory)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")