class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            print(f"Item with ID {item_id} already exists.")
        else:
            self.items[item_id] = {'name': name, 'quantity': quantity, 'price': price}

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
        else:
            print(f"No item found with ID {item_id}.")

    def update_item(self, item_id, name=None, quantity=None, price=None):
        if item_id in self.items:
            if name:
                self.items[item_id]['name'] = name
            if quantity and quantity.isdigit():
                self.items[item_id]['quantity'] = int(quantity)
            if price and price.replace('.', '', 1).isdigit():
                self.items[item_id]['price'] = float(price)
        else:
            print(f"No item found with ID {item_id}.")

    def list_items(self):
        for item_id, info in self.items.items():
            print(f"ID: {item_id}, Name: {info['name']}, Quantity: {info['quantity']}, Price: ${info['price']}")

    def search_by_name(self, name):
        found_items = [info for info in self.items.values() if name.lower() in info['name'].lower()]
        if not found_items:
            print("No items found.")
        for item in found_items:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']}")

    def calculate_inventory_value(self):
        total_value = sum(info['quantity'] * info['price'] for info in self.items.values())
        print(f"Total inventory value: ${total_value}")

    def save_inventory(self, filename='inventory.txt'):
        with open(filename, 'w') as file:
            for item_id, info in self.items.items():
                file.write(f"{item_id},{info['name']},{info['quantity']},{info['price']}\n")

    def load_inventory(self, filename='inventory.txt'):
        with open(filename, 'r') as file:
            for line in file:
                item_id, name, quantity, price = line.strip().split(',')
                self.items[item_id] = {'name': name, 'quantity': int(quantity), 'price': float(price)}

def main():
    inventory = Inventory()
    inventory.load_inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. List All Items")
        print("5. Search by Name")
        print("6. Show Inventory Value")
        print("7. Save Inventory")
        print("8. Exit")
        choice = input("Enter choice: ")

        try:
            choice = int(choice)
            if choice == 1:
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                quantity = input("Enter quantity: ")
                price = input("Enter price per unit: ")
                inventory.add_item(item_id, name, quantity, price)
            elif choice == 2:
                item_id = input("Enter item ID to remove: ")
                inventory.remove_item(item_id)
            elif choice == 3:
                item_id = input("Enter item ID to update: ")
                name = input("Enter new name (press enter to skip): ")
                quantity = input("Enter new quantity (press enter to skip): ")
                price = input("Enter new price per unit (press enter to skip): ")
                inventory.update_item(item_id, name, quantity, price)
            elif choice == 4:
                inventory.list_items()
            elif choice == 5:
                name = input("Enter name to search for: ")
                inventory.search_by_name(name)
            elif choice == 6:
                inventory.calculate_inventory_value()
            elif choice == 7:
                inventory.save_inventory()
            elif choice == 8:
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()
