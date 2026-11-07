# MISIS_VVS_MANAKOVA_MARIA

Учебный репозиторий для курса ВВС в МИСИС.

## Projects

| # | Project | Description |
|---|---|---|
| 01 | [Calculators](https://github.com/mysthz/MISIS_VVS_MANAKOVA_MARIA/tree/main/projects/01-calculators) | Four implementations exploring different approaches to calculations, including functions and object-oriented programming. |
| 02 | [String Methods Explorer](https://github.com/mysthz/MISIS_VVS_MANAKOVA_MARIA/tree/main/projects/02-string-methods) | Interactive exploration of Python string methods and text normalization. |
| 03 | [Maze Game](https://github.com/mysthz/MISIS_VVS_MANAKOVA_MARIA/tree/main/projects/03-maze-game) | A console-based RPG game featuring maze exploration, inventory management, traps, monsters, and random events. |
| 04 | [Titanic Data Analysis with Pandas and NumPy](https://github.com/mysthz/MISIS_VVS_MANAKOVA_MARIA/tree/main/projects/04-titanic) | Data cleaning, filtering, grouping, and statistical analysis of the Titanic dataset using Pandas and NumPy.

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

### 04. Titanic Data Analysis with Pandas and NumPy

A practical project focused on loading, processing, filtering, and analyzing tabular data using Python libraries **Pandas** and **NumPy**.

The project uses the Titanic dataset to explore passenger information, handle missing values, perform statistical calculations, and identify patterns in survival rates.

### Main features

- **Data Loading and Exploration** — loading CSV data into a Pandas DataFrame, examining its structure, columns, and data types.
- **Statistical Analysis** — calculating mean, median, minimum, maximum, and standard deviation for numerical features.
- **Missing Values Handling** — identifying missing data, filling missing ages with the median, and removing columns with a high percentage of missing values.
- **Data Analysis with NumPy** — calculating survival rates, average ages, and ticket prices.
- **Data Filtering** — selecting passengers based on age, gender, passenger class, survival status, and port of embarkation.
- **Grouping and Aggregation** — analyzing passenger statistics by class, gender, and embarkation port.
- **Data Export** — saving the processed dataset and grouped statistics to CSV files.

### Technologies

- Python
- Pandas
- NumPy

### Output files

- `titanic_processed.csv` — cleaned and processed dataset.
- `titanic_statistics.csv` — grouped passenger statistics by class and gender.
