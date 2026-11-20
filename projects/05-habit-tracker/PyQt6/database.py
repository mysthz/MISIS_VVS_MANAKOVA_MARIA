
import sqlite3


connection = sqlite3.connect("habits.db")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()


# Таблица привычек
cursor.execute("""
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    completed INTEGER DEFAULT 0
)
""")


# Таблица категорий
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_id INTEGER,
    category TEXT,
    FOREIGN KEY (habit_id) REFERENCES habits(id)
)
""")

connection.commit()


# Добавление привычки
def add_habit(name):
    cursor.execute(
        "INSERT INTO habits (name) VALUES (?)",
        (name,)
    )
    connection.commit()


# Получение всех привычек
def get_habits():
    cursor.execute("SELECT * FROM habits")
    return cursor.fetchall()


# Отметка выполнения
def mark_done(habit_id):
    cursor.execute(
        "UPDATE habits SET completed = 1 WHERE id = ?",
        (habit_id,)
    )
    connection.commit()


# Удаление привычки
def delete_habit(habit_id):
    cursor.execute(
        "DELETE FROM categories WHERE habit_id = ?",
        (habit_id,)
    )

    cursor.execute(
        "DELETE FROM habits WHERE id = ?",
        (habit_id,)
    )

    connection.commit()
