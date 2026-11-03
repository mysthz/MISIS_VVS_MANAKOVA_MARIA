
import pandas as pd
import numpy as np


# Часть 2

df = pd.read_csv('tested.csv')
print('часть 2')

# Задание 7. Вывод первых n строк
print('\nПервые строки таблицы:')

n = int(input('Введите количество строк: '))
print(df.head(n))


# Задание 8. Вывод последних пяти строк
print('\nПоследние пять строк:')
print(df.tail())


# Задание 9. Размер таблицы
print('\nРазмер таблицы:')
rows_before = df.shape[0]
columns_before = df.shape[1]
print(f'Количество строк: {rows_before}, количество столбцов: {columns_before}')


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
    return df[column].sum() / (len(df)-df[column].isna().sum())


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


# Часть 3
print('\nчасть 3')

# Задание 16. Количество пропусков в каждом столбце
print('\nКоличество пропусков: ')
for column in df.columns:
    print(f'Количество пропусков в {column}: {df[column].isna().sum()}')


# Задание 17. Процент пропусков относительно общего числа строк.
print('\nПроцент пропусков: ')
for column in df.columns:
    print(f'Процент пропусков в {column}: {df[column].isna().sum()/len(df)*100:.2f}%')

# Задание 18. Cтолбец с максимальным количеством пропусков
print('\nМаксимальное кол-во пропусков:')
missing = df.isna().sum()

print(f'Столбец: {missing.idxmax()}')
print(f'Количество пропусков: {missing.max()}')

# Задание 19. для Age среднее, медиану, минимум, максимум, стандартное отклонение и количество известных значений.
age_middle_before = middle_value('Age')
age_median_before = median_value('Age')
age_min_before = min_value('Age')
age_max_before = max_value('Age')
age_std_before = standart_deviation('Age')
age_count_before = 418 - df['Age'].isna().sum()

# Задание 20. Заполнение пропусков
df['Age'] = df['Age'].fillna(median_value('Age'))

# Задание 21. Повторный расчет характеристик
age_middle_after = middle_value('Age')
age_median_after = median_value('Age')
age_min_after = min_value('Age')
age_max_after = max_value('Age')
age_std_after = standart_deviation('Age')
age_count_after = df['Age'].count()

# Задание 22. Таблица
data1 = {
    'Показатель': ['Среднее арифметическое', 'Медиана', 'Минимальный возраст', 'Максимальный возраст', 'Стандартное отклонение', 'Количество известных значений'],
    'До обработки': [age_middle_before, age_median_before, age_min_before, age_max_before, age_std_before, age_count_before],
    'После обработки': [age_middle_after, age_median_after, age_min_after, age_max_after, age_std_after, age_count_after]
         }

print('\n', pd.DataFrame(data1))

# Задание 23. Удаление строк с отсутствующим Embarked
df = df.dropna(subset=['Embarked'])

# Задание 24. Доля пропусков в Cabin
a = df['Cabin'].isna().sum()/len(df) * 100
print(f'\nДоля пропусков в Cabin: {a:.2f}%')

if a>50:
    df = df.drop(columns=['Cabin'])
    print('Столбец Cabin удалён.')

# Задание 25. Проверка, что осталось
print('\nОставшиеся пропуски:')
print(df.isna().sum())

#Задание 26. Сравнение размера таблицы до и после обработки
print('\nРазмер таблицы:')
print(f'До обработки: строк — {rows_before}, столбцов — {columns_before}')
print(f'После обработки: строк — {df.shape[0]}, столбцов — {df.shape[1]}')

"""Контрольные вопросы
27. тк на неё не влияют слишком большие или маленькие значения.
28. изменились среднее арифметическое, стандартное отклонение и количество известных значений. медиана, минимальный и максимальный возраст остались прежними, тк пропуски заполнялись значением медианы, которое уже было в данных.
29. стандартное отклонение показывает, насколько сильно значения отличаются друг от друга, после заполнения медианой добавляется больше одинаковых значений поэтому разброс меняется
30. нет тк после заполнения пропусков становится больше пассажиров с возрастом, равным медиане и из-за этого меняется частота этого значения и общее распределение возрастов
"""

#Часть 4
# Задание 31. Общий процент выживших
survived_percent = np.sum(df['Survived'] == 1) / len(df) * 100


# Задание 32. Процент выживших отдельно среди мужчин и женщин
female_percent = np.sum((df['Survived'] == 1) & (df['Sex'] == 'female')) / np.sum(df['Sex'] == 'female') * 100
male_percent = np.sum((df['Survived'] == 1) & (df['Sex'] == 'male')) / np.sum(df['Sex'] == 'male') * 100


# Задание 33. Средний возраст мужчин и женщин
average_age_female = np.mean(df[df['Sex'] == 'female']['Age'])
average_age_male = np.mean(df[df['Sex'] == 'male']['Age'])


# Задание 34. Средний  возраст выживших и погибших отдельно для мужчин и женщин.
average_age_survived_female = np.mean(df[(df['Sex']=='female') & (df['Survived']==1)]['Age'])
average_age_survived_male = np.mean(df[(df['Sex']=='male') & (df['Survived']==1)]['Age'])
average_age_notsurvived_female = np.mean(df[(df['Sex']=='female') & (df['Survived']==0)]['Age'])
average_age_notsurvived_male = np.mean(df[(df['Sex']=='male') & (df['Survived']==0)]['Age'])


# Задание 35. Минимальная, максимальная и средная стоимость билета
max_ticket_cost = np.nanmax(df['Fare'])
min_ticket_cost = np.nanmin(df['Fare'])
average_ticket_cost = np.nanmean(df['Fare'])


# Задание 36. Cтандартное отклонение возраста
standart_age_deviation = np.nanstd(df['Age'])


#Таблица
# Результаты анализа с помощью NumPy
data_numpy = {
    'Показатель': [
        'Общий процент выживших',
        'Процент выживших женщин',
        'Процент выживших мужчин',
        'Средний возраст женщин',
        'Средний возраст мужчин',
        'Средний возраст выживших женщин',
        'Средний возраст погибших женщин',
        'Средний возраст выживших мужчин',
        'Средний возраст погибших мужчин',
        'Минимальная стоимость билета',
        'Максимальная стоимость билета',
        'Средняя стоимость билета',
        'Стандартное отклонение возраста'
    ],
    'Значение': [
        survived_percent,
        female_percent,
        male_percent,
        average_age_female,
        average_age_male,
        average_age_survived_female,
        average_age_notsurvived_female,
        average_age_survived_male,
        average_age_notsurvived_male,
        min_ticket_cost,
        max_ticket_cost,
        average_ticket_cost,
        standart_age_deviation
    ]
}

print('\nРезультаты анализа:')
print(pd.DataFrame(data_numpy))


#Часть 5

