from inventory import Inventory


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.is_alive = True
        self.has_key = False
        self.visited = []
        self.inventory = Inventory()

    def take_damage(self, damage):
        if self.is_alive:
            self.health -= damage

            if self.health <= 0:
                self.health = 0
                self.is_alive = False
                print('You died')

    def heal(self, amount):
        if not self.is_alive:
            print('You cannot heal. You are dead!')
            return False

        if self.health >= 100:
            print('Your health is already full!')
            return False

        self.health += amount

        if self.health > 100:
            self.health = 100

        print(f'You healed! Your current HP: {self.health}')
        return True

    def get_key(self):
        self.has_key = True
        print('You have found the key')