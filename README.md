# MISIS_VVS_MANAKOVA_MARIA

Учебный репозиторий для курса ВВС в МИСИС.

## Projects

| # | Project | Description |
|---|---|---|
| 01 | [Calculators](https://github.com/mysthz/MISIS_VVS_MANAKOVA_MARIA/tree/main/projects/01-calculators) | Four implementations exploring different approaches to calculations, including functions and object-oriented programming. |
| 02 | [String Methods Explorer](https://github.com/mysthz/MISIS_VVS_MANAKOVA_MARIA/tree/main/projects/02-string-methods) | Interactive exploration of Python string methods and text normalization. |
| 03 | [Maze Game](https://github.com/mysthz/MISIS_VVS_MANAKOVA_MARIA/tree/main/projects/03-maze-game) | A console-based RPG game featuring maze exploration, inventory management, traps, monsters, and random events. |

### 01. Calculators

Four implementations demonstrating different programming approaches:

1. Sequential calculator.
2. Calculator with a separate function for each operation.
3. Calculator using a single function for multiple operations.
4. Work-life balance calculator demonstrating classes, inheritance, and object-oriented programming.

### 02. String Methods Explorer

An interactive program for exploring built-in Python string methods. The user selects a difficulty level and then chooses a method to see a demonstration and test it on custom input.

The project is divided into five levels:

1. **Case Conversion** — `upper()`, `lower()`, `capitalize()`.
2. **Searching and Replacing** — `find()`, `replace()`, `count()`.
3. **Splitting and Joining** — `split()`, `join()`.
4. **String Validation and Cleaning** — `isdigit()`, `isalpha()`, `strip()`.
5. **Text Normalization** — a custom `normalize()` function combining several string operations.

### 03. Maze Game

A console-based RPG game written in Python. The player explores a maze, visits different rooms, collects items, fights monsters, and tries to find the exit.

The main objective is to find a key and escape from the maze while keeping the player's health above zero.

**Main features:**

- **Maze exploration** — movement through a two-dimensional maze with coordinates and a map displaying visited rooms.
- **Player system** — health points (HP), inventory, key collection, and character status.
- **Room interactions** — empty rooms, traps, chests, portals, monsters, keys, and exits.
- **Inventory management** — collecting and using weapons, armor, and healing potions.
- **Combat system** — fighting monsters with a weapon or escaping from encounters.
- **Equipment mechanics** — weapons allow the player to attack, while armor reduces incoming damage.
- **Random events** — chests contain randomly selected items, and portals teleport the player to random rooms.
- **Game conditions** — winning by finding the key and reaching the exit, or losing when the player's HP reaches zero.

**Project structure:**

- `main.py` — main game loop and interaction between game components.
- `maze.py` — maze generation, player movement, and map display.
- `player.py` — player class and character attributes.
- `rooms.py` — room classes and their interactions.
- `inventory.py` — inventory management.
