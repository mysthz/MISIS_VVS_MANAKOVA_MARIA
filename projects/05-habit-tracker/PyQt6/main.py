
import sys
from PyQt6.QtWidgets import *


class HabitTracker(QWidget):

    def __init__(self):
        super().__init__()

        self.habits = []

        self.setWindowTitle("My Habits")
        self.setFixedSize(500, 550)
        self.setStyleSheet("background-color: #F4F5F7;")

        self.create_interface()

    def create_interface(self):
        # Заголовок
        self.title = QLabel("My Habits")
        self.title.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: #333333;"
        )

        # Подпись для поля ввода
        self.input_label = QLabel("Введите новую привычку:")

        # Поле ввода
        self.entry = QLineEdit()

        # Кнопка добавления
        self.add_button = QPushButton("Добавить привычку")
        self.add_button.setStyleSheet("background-color: #A8D5BA;")
        self.add_button.clicked.connect(self.add_habit)

        # Подпись списка
        self.list_label = QLabel("Мои привычки:")

        # Чекбокс фильтрации
        self.filter_checkbox = QCheckBox(
            "Показывать только невыполненные"
        )
        self.filter_checkbox.toggled.connect(self.filter_habits)

        # Список привычек
        self.habit_list = QListWidget()

        # Кнопка выполнения
        self.done_button = QPushButton("Отметить выполнение")
        self.done_button.setStyleSheet("background-color: #B8D8E8;")
        self.done_button.clicked.connect(self.mark_done)

        # Кнопка удаления
        self.delete_button = QPushButton("Удалить привычку")
        self.delete_button.setStyleSheet("background-color: #F2B8B5;")
        self.delete_button.clicked.connect(self.delete_habit)

        # Счётчик
        self.counter_label = QLabel("Выполнено: 0 из 0")
        self.counter_label.setStyleSheet(
            "font-size: 14px; font-weight: bold; color: #4A8060;"
        )

        # Размещение элементов
        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.input_label)
        layout.addWidget(self.entry)
        layout.addWidget(self.add_button)
        layout.addWidget(self.list_label)
        layout.addWidget(self.filter_checkbox)
        layout.addWidget(self.habit_list)
        layout.addWidget(self.done_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.counter_label)

        self.setLayout(layout)

    def add_habit(self):
        name = self.entry.text().strip()

        if not name:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Введите привычку!"
            )
            return

        self.habits.append(name)

        self.entry.clear()

        self.filter_habits()
        self.update_counter()

    def mark_done(self):
        selected = self.habit_list.currentRow()

        if selected == -1:
            QMessageBox.information(
                self,
                "Информация",
                "Выберите привычку!"
            )
            return

        name = self.habits[selected]

        if not name.startswith("✓"):
            self.habits[selected] = "✓ " + name

        self.filter_habits()
        self.update_counter()

    def delete_habit(self):
        selected = self.habit_list.currentRow()

        if selected == -1:
            QMessageBox.information(
                self,
                "Информация",
                "Выберите привычку!"
            )
            return

        self.habits.pop(selected)

        self.filter_habits()
        self.update_counter()

    def update_counter(self):
        total = len(self.habits)
        done = sum(1 for habit in self.habits if habit.startswith("✓"))

        self.counter_label.setText(
            f"Выполнено: {done} из {total}"
        )

    # Функция фильтрации привычек

    def filter_habits(self):
        self.habit_list.clear()

        for habit in self.habits:
            if self.filter_checkbox.isChecked() and habit.startswith("✓"):
                continue

            self.habit_list.addItem(habit)


app = QApplication(sys.argv)

window = HabitTracker()
window.show()

sys.exit(app.exec())
