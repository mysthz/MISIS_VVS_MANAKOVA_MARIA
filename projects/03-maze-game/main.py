from maze import player_move, first_maze, display_maze
from player import Player
from rooms import trap1, trap2, trap3
from rooms import monster
from rooms import chest1, chest2, chest3, portal


print("""
   Available commands:

   MOVEMENT:
   up    - move up
   down  - move down
   left  - move left
   right - move right

   INVENTORY:
   inventory  - show inventory
   use potion - restore 30 HP
   health - show current HP

   OTHER:
   help - show available commands

   During monster encounter:
   attack - attack the monster
   run    - escape from the monster
   """)


player = Player(0, 0)
player.visited.append([player.x, player.y])

display_maze(player.x, player.y, player.visited)


while player.is_alive:
    command = input("Where would you like to go? ").lower()

    if command == 'help':
        print("""
    Available commands:

    MOVEMENT:
    up    - move up
    down  - move down
    left  - move left
    right - move right

    INVENTORY:
    inventory  - show inventory
    use potion - restore 30 HP
    health - show current HP

    OTHER:
    help - show available commands

    During monster encounter:
    attack - attack the monster
    run    - escape from the monster
    """)
        continue

    if command == 'use potion':
        if 'potion' in player.inventory.inventory:
            if player.heal(30):
                player.inventory.remove_item('potion')
        else:
            print("You don't have any potions!")

        continue

    if command == 'inventory':
        player.inventory.show_inventory()
        continue

    if command == 'health':
        print(f'Your current HP: {player.health}/100')
        continue

    player.x, player.y, room = player_move(
        player.x, player.y, command
    )

    # Portal
    if room == "portal":
        while room == "portal":
            if [player.x, player.y] not in player.visited:
                player.visited.append([player.x, player.y])

            player.x, player.y, room = portal.teleport(
                first_maze, player.x, player.y
            )

        if [player.x, player.y] not in player.visited:
            player.visited.append([player.x, player.y])

    # Key
    if room == "key" and not player.has_key:
        player.get_key()

    # Monster
    if room == "monster":
        monster.trigger()

        while monster.state == 'active':
            command = input("Attack or run? ").lower()
            escaped = monster.action(command, player)

            if not player.is_alive:
                break

            if escaped:
                if [player.x, player.y] not in player.visited:
                    player.visited.append([player.x, player.y])

                player.x += 1

                if [player.x, player.y] not in player.visited:
                    player.visited.append([player.x, player.y])

                room = first_maze[player.y][player.x]
                break

    # Trap
    if room == "trap":
        if player.x == 1 and player.y == 2:
            trap1.catch(player)

        elif player.x == 2 and player.y == 5:
            trap2.catch(player)

        elif player.x == 1 and player.y == 0:
            trap3.catch(player)

    # Chest
    if room == "chest":
        item = None

        if player.x == 4 and player.y == 1:
            item = chest1.open()

        elif player.x == 0 and player.y == 3:
            item = chest2.open()

        elif player.x == 5 and player.y == 4:
            item = chest3.open()

        if item is not None and item != 'nothing':
            player.inventory.add_item(item)

        player.inventory.show_inventory()

    # Mark visited room
    if [player.x, player.y] not in player.visited:
        player.visited.append([player.x, player.y])

    # Check death
    if not player.is_alive:
        print("Game over!")
        break

    # Check exit
    if room == "exit":
        if player.has_key:
            print("You find exit! Win!")
            break
        else:
            print("You need a key to open the exit!")

    display_maze(player.x, player.y, player.visited)

    print(f"Your current position is {player.x}, {player.y}")