
import pandas as pd
import numpy as np


# Часть 2

df = pd.read_csv('tested.csv')


# Задание 7. Вывод первых n строк
print('\nПервые строки таблицы:')

n = int(input('Введите количество строк: '))
print(df.head(n))


# Задание 8. Вывод последних пяти строк
print('\nПоследние пять строк:')
print(df.tail())


# Задание 9. Размер таблицы
print('\nРазмер таблицы:')
print(f'Количество строк: {df.shape[0]}, количество столбцов: {df.shape[1]}')


# Задание 10. Названия столбцов
print('\nНазвания столбцов:')
print(*df.columns, sep=', ')


# Задание 11. Типы данных
print('\nТипы данных:')
print(df.dtypes)


# Задание 12. Разделение признаков на числовые и категориальные
numeric_columns = ['Age', 'Fare', 'SibSp', 'Parch']

categorical_columns = ['PassengerId', 'Survived', 'Pclass',
                       'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']

print('\nЧисловые признаки:')
print(numeric_columns)

print('\nКатегориальные признаки:')
print(categorical_columns)


# Задание 13. Статистические характеристики числовых признаков

def middle_value(column):
    return df[column].sum() / (418-df[column].isna().sum())


def median_value(column):
    return df[column].median()


def min_value(column):
    return df[column].min()


def max_value(column):
    return df[column].max()


def standart_deviation(column):
    return df[column].std()


data = {
    'Характеристика': ['Среднее значение', 'Медиана', 'Минимум', 'Максимум', 'Стандартное отклонение'],
    'Age': [middle_value('Age'), median_value('Age'), min_value('Age'), max_value('Age'), standart_deviation('Age')],
    'Fare': [middle_value('Fare'), median_value('Fare'), min_value('Fare'), max_value('Fare'), standart_deviation('Fare')],
    'SibSp': [middle_value('SibSp'), median_value('SibSp'), min_value('SibSp'), max_value('SibSp'), standart_deviation('SibSp')],
    'Parch': [middle_value('Parch'), median_value('Parch'), min_value('Parch'), max_value('Parch'),
              standart_deviation('Parch')]
}

print('\nСтатистические характеристики:')
print(pd.DataFrame(data))


# Задание 14. Количество пассажиров каждого класса
print('\nКоличество пассажиров по классам:')

classes = df['Pclass'].value_counts()

for class_number, value in classes.items():
    print(f'Количество пассажиров {class_number}-го класса: {value}')


# Задание 15. Количество уникальных значений Embarked
print('\nУникальные значения Embarked:')
print('Количество уникальных значений:', df['Embarked'].nunique())


