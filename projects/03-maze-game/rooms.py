import random

class Room:
    def __init__(self, room_type, state):
        self.room_type = room_type
        self.state = state

class Chest(Room):
    def __init__(self):
        super().__init__("chest", "inactive")
    def open(self):
        if self.state == 'active':
            print('You have already opened the chest. It is empty')

        elif self.state == 'inactive':
            self.state = 'active'
            items = ['weapon', 'armor', 'potion', 'nothing']
            item = random.choice(items)
            print(f'You open the chest! Grab {item}')
            return item

chest1 = Chest()
chest2 = Chest()
chest3 = Chest()

class Trap(Room):
    def __init__(self):
        super().__init__("trap", "active")
    def catch(self, player):
        if self.state == 'active':
            player.take_damage(15)
            self.state = 'inactive'
            print('You catch the trap. -15 to your hp')
            print(f'Your current hp is {player.health}')
        elif self.state == 'inactive':
            print('You have already caught the trap. It does not work')

trap1 = Trap()
trap2 = Trap()
trap3 = Trap()

class Monster(Room):
    def __init__(self):
        super().__init__("monster", "active")
        self.hp = 30

    def trigger(self):
        if self.state == 'active':
            print('You are in the monster room.')

    def action(self, command, player):
        if self.state == 'inactive':
            return False

        if command == 'run':
            print('You have run out of the monster room.')
            return True

        elif command == 'attack':
            if 'weapon' not in player.inventory.inventory:
                print("You don't have a weapon! You must run away.")
                return False

            target = input('Where do you want to hit the monster? (arm, leg, chest, tail): ').lower()

            if target not in ['arm', 'leg', 'chest', 'tail']:
                print('Choose a valid body part!')
                return False

            print(f'You attack the monster in the {target}!')
            self.hp -= 10

            if self.hp <= 0:
                self.hp = 0
                self.state = 'inactive'
                print('You defeated the monster!')
            else:
                print(f'You hit the monster! {self.hp} hp left.')

                monster_target = random.choice(['arm', 'leg', 'chest', 'tail'])
                print(f'The monster hits you in the {monster_target}!')

                if 'armor' in player.inventory.inventory:
                    player.take_damage(15)
                else:
                    player.take_damage(30)

                print(f'Your current hp is {player.health}')

        return False
monster = Monster()

class Portal(Room):
    def __init__(self):
        super().__init__("portal", "active")

    def teleport(self, maze, player_x, player_y):
        print('You are in portal room.')
        possible_rooms = []

        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if (x, y) != (player_x, player_y):
                    possible_rooms.append((x, y))

        destination = random.choice(possible_rooms)

        new_x, new_y = destination
        room = maze[new_y][new_x]

        print('The portal teleports you to another room!')

        return new_x, new_y, room

portal = Portal()

class Exit(Room):
    def __init__(self):
        super().__init__("exit", "active")

    def leave(self, player):
        if player.has_key:
            print('You unlocked the exit! You win!')
            return True
        else:
            print('The exit is locked. You need a key!')
            return False



