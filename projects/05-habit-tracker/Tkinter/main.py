
import tkinter as tk
from tkinter import messagebox


# Главное окно

window = tk.Tk()

window.title("My Habits")
window.geometry("500x500")
window.configure(bg="#F4F5F7")
window.resizable(False, False)


# Список привычек

habits = []

# Переменная для фильтрации

show_only_active = tk.BooleanVar(value=False)


# Функция добавления привычки

def add_habit():
    name = entry.get().strip()

    if not name:
        messagebox.showwarning("Ошибка", "Введите привычку!")
        return

    habits.append(name)

    filter_habits()

    entry.delete(0, tk.END)

    update_counter()


# Функция отметки выполнения

def mark_done():
    selected = habit_list.curselection()

    if not selected:
        messagebox.showinfo("Информация", "Выберите привычку!")
        return

    index = selected[0]
    name = habits[index]

    habits[index] = "✓ " + name

    filter_habits()
    update_counter()


# Функция удаления привычки

def delete_habit():
    selected = habit_list.curselection()

    if not selected:
        messagebox.showinfo("Информация", "Выберите привычку!")
        return

    index = selected[0]

    habits.pop(index)

    filter_habits()
    update_counter()


# Функция обновления счётчика

def update_counter():
    total = len(habits)
    done = sum(1 for habit in habits if habit.startswith("✓"))

    counter_label.config(
        text=f"Выполнено: {done} из {total}"
    )


# Функция фильтрации привычек

def filter_habits():
    habit_list.delete(0, tk.END)

    for habit in habits:
        if show_only_active.get() and habit.startswith("✓"):
            continue

        habit_list.insert(tk.END, habit)


# Заголовок

title = tk.Label(
    window,
    text="My Habits",
    font=("Arial", 24, "bold"),
    bg="#F4F5F7",
    fg="#333333"
)
title.pack(pady=20)


# Поле ввода

input_label = tk.Label(
    window,
    text="Введите новую привычку:",
    font=("Arial", 12),
    bg="#F4F5F7"
)
input_label.pack(pady=5)


entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 12)
)
entry.pack(pady=5)


# Кнопка добавления

add_button = tk.Button(
    window,
    text="Добавить привычку",
    font=("Arial", 11),
    bg="#A8D5BA",
    command=add_habit
)
add_button.pack(pady=10)


# Список привычек

list_label = tk.Label(
    window,
    text="Мои привычки:",
    font=("Arial", 14, "bold"),
    bg="#F4F5F7"
)
list_label.pack(pady=10)


# Выбор параметров

filter_checkbox = tk.Checkbutton(
    window,
    text="Показывать только невыполненные",
    variable=show_only_active,
    command=filter_habits,
    font=("Arial", 10),
    bg="#F4F5F7"
)
filter_checkbox.pack(pady=5)


habit_list = tk.Listbox(
    window,
    width=45,
    height=10,
    font=("Arial", 11)
)
habit_list.pack(pady=5)


# Кнопки управления

done_button = tk.Button(
    window,
    text="Отметить выполнение",
    font=("Arial", 10),
    bg="#B8D8E8",
    command=mark_done
)
done_button.pack(pady=5)


delete_button = tk.Button(
    window,
    text="Удалить привычку",
    font=("Arial", 10),
    bg="#F2B8B5",
    command=delete_habit
)
delete_button.pack(pady=5)


# Счётчик выполнения

counter_label = tk.Label(
    window,
    text="Выполнено: 0 из 0",
    font=("Arial", 12, "bold"),
    bg="#F4F5F7",
    fg="#4A8060"
)
counter_label.pack(pady=10)


# Запуск программы

window.mainloop()
