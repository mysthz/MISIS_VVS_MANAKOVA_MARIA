class Inventory:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty!")
        else:
            print("Your inventory:", self.inventory)