first_maze = [
    ["empty", "trap", "monster", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "chest", "empty"],
    ["empty", "trap", "empty", "empty", "empty", "empty"],
    ["chest", "empty", "empty", "portal", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "key", "chest"],
    ["empty", "empty", "trap", "empty", "empty", "exit"]
]

def player_move(player_x, player_y, command):
    new_x = player_x
    new_y = player_y

    if command == 'left':
        new_x -= 1
    elif command == 'right':
        new_x += 1
    elif command == 'up':
        new_y -= 1
    elif command == 'down':
        new_y += 1
    else:
        print("Unknown command!")
        return player_x, player_y, first_maze[player_y][player_x]

    if (new_x < 0 or new_x >= len(first_maze[0]) or new_y < 0 or new_y >= len(first_maze)):
        print("Wall!")
        return player_x, player_y, first_maze[player_y][player_x]
    if first_maze[new_y][new_x] == 'wall':
        print("Wall! Go around!")
        return player_x, player_y, first_maze[player_y][player_x]

    return new_x, new_y, first_maze[new_y][new_x]

def display_maze(player_x, player_y, visited):
    for y in range(len(first_maze)):
        for x in range(len(first_maze[0])):
            if [x, y] == [player_x, player_y]:
                print('@', end=' ')
            elif [x, y] not in visited:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print()