import pandas as pd
import numpy as np


# Часть 2

df = pd.read_csv('tested.csv')
print('часть 2')

# Задание 7. Вывод первых n строк
print('\nПервые строки таблицы:')

number_of_rows = int(input('Введите количество строк: '))
print(df.head(number_of_rows))


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

def mean_value(column):
    return df[column].sum() / (len(df) - df[column].isna().sum())


def median_value(column):
    return df[column].median()


def min_value(column):
    return df[column].min()


def max_value(column):
    return df[column].max()


def standard_deviation(column):
    return df[column].std()


numeric_statistics = {
    'Характеристика': ['Среднее значение', 'Медиана', 'Минимум', 'Максимум', 'Стандартное отклонение'],
    'Age': [mean_value('Age'), median_value('Age'), min_value('Age'), max_value('Age'),
            standard_deviation('Age')],
    'Fare': [mean_value('Fare'), median_value('Fare'), min_value('Fare'), max_value('Fare'),
             standard_deviation('Fare')],
    'SibSp': [mean_value('SibSp'), median_value('SibSp'), min_value('SibSp'), max_value('SibSp'),
              standard_deviation('SibSp')],
    'Parch': [mean_value('Parch'), median_value('Parch'), min_value('Parch'), max_value('Parch'),
              standard_deviation('Parch')]
}

print('\nСтатистические характеристики:')
print(pd.DataFrame(numeric_statistics))


# Задание 14. Количество пассажиров каждого класса
print('\nКоличество пассажиров по классам:')

passengers_by_class = df['Pclass'].value_counts()

for class_number, value in passengers_by_class.items():
    print(f'Количество пассажиров {class_number}-го класса: {value}')


# Задание 15. Количество уникальных значений Embarked
print('\nУникальные значения Embarked:')
print('Количество уникальных значений:', df['Embarked'].nunique())

# Контрольный вопрос
# Pclass содержит числа, но обозначает категории пассажиров:
# первый, второй и третий класс. Поэтому его рассматривают
# как категориальный признак.

# Часть 3
print('\nчасть 3')


# Задание 16. Количество пропусков в каждом столбце
print('\nКоличество пропусков: ')
for column in df.columns:
    print(f'Количество пропусков в {column}: {df[column].isna().sum()}')


# Задание 17. Процент пропусков относительно общего числа строк
print('\nПроцент пропусков: ')
for column in df.columns:
    print(f'Процент пропусков в {column}: {df[column].isna().sum() / len(df) * 100:.2f}%')


# Задание 18. Столбец с максимальным количеством пропусков
print('\nМаксимальное кол-во пропусков:')
missing_values = df.isna().sum()

print(f'Столбец: {missing_values.idxmax()}')
print(f'Количество пропусков: {missing_values.max()}')


# Задание 19. Характеристики Age до обработки
age_mean_before = mean_value('Age')
age_median_before = median_value('Age')
age_min_before = min_value('Age')
age_max_before = max_value('Age')
age_std_before = standard_deviation('Age')
age_count_before = len(df) - df['Age'].isna().sum()


# Задание 20. Заполнение пропусков
df['Age'] = df['Age'].fillna(median_value('Age'))


# Задание 21. Повторный расчет характеристик
age_mean_after = mean_value('Age')
age_median_after = median_value('Age')
age_min_after = min_value('Age')
age_max_after = max_value('Age')
age_std_after = standard_deviation('Age')
age_count_after = df['Age'].count()


# Задание 22. Таблица
age_statistics_comparison = {
    'Показатель': ['Среднее арифметическое', 'Медиана', 'Минимальный возраст',
                   'Максимальный возраст', 'Стандартное отклонение',
                   'Количество известных значений'],
    'До обработки': [age_mean_before, age_median_before, age_min_before,
                     age_max_before, age_std_before, age_count_before],
    'После обработки': [age_mean_after, age_median_after, age_min_after,
                        age_max_after, age_std_after, age_count_after]
}

print('\n', pd.DataFrame(age_statistics_comparison))


# Задание 23. Удаление строк с отсутствующим Embarked
df = df.dropna(subset=['Embarked'])


# Задание 24. Доля пропусков в Cabin
cabin_missing_percent = df['Cabin'].isna().sum() / len(df) * 100
print(f'\nДоля пропусков в Cabin: {cabin_missing_percent:.2f}%')

if cabin_missing_percent > 50:
    df = df.drop(columns=['Cabin'])
    print('Столбец Cabin удалён.')


# Задание 25. Проверка оставшихся пропусков
print('\nОставшиеся пропуски:')
print(df.isna().sum())


# Задание 26. Сравнение размера таблицы до и после обработки
print('\nРазмер таблицы:')
print(f'До обработки: строк — {rows_before}, столбцов — {columns_before}')
print(f'После обработки: строк — {df.shape[0]}, столбцов — {df.shape[1]}')


"""Контрольные вопросы
27. тк на неё не влияют слишком большие или маленькие значения.
28. изменились среднее арифметическое, стандартное отклонение и количество известных значений. медиана, минимальный и максимальный возраст остались прежними, тк пропуски заполнялись значением медианы, которое уже было в данных.
29. стандартное отклонение показывает, насколько сильно значения отличаются друг от друга, после заполнения медианой добавляется больше одинаковых значений поэтому разброс меняется
30. нет тк после заполнения пропусков становится больше пассажиров с возрастом, равным медиане и из-за этого меняется частота этого значения и общее распределение возрастов
"""


# Часть 4

# Задание 31. Общий процент выживших
survived_percent = np.sum(df['Survived'] == 1) / len(df) * 100


# Задание 32. Процент выживших отдельно среди мужчин и женщин
female_percent = np.sum((df['Survived'] == 1) & (df['Sex'] == 'female')) / np.sum(df['Sex'] == 'female') * 100
male_percent = np.sum((df['Survived'] == 1) & (df['Sex'] == 'male')) / np.sum(df['Sex'] == 'male') * 100


# Задание 33. Средний возраст мужчин и женщин
average_age_female = np.mean(df[df['Sex'] == 'female']['Age'])
average_age_male = np.mean(df[df['Sex'] == 'male']['Age'])


# Задание 34. Средний возраст выживших и погибших отдельно для мужчин и женщин
average_age_survived_female = np.mean(df[(df['Sex'] == 'female') & (df['Survived'] == 1)]['Age'])
average_age_survived_male = np.mean(df[(df['Sex'] == 'male') & (df['Survived'] == 1)]['Age'])
average_age_notsurvived_female = np.mean(df[(df['Sex'] == 'female') & (df['Survived'] == 0)]['Age'])
average_age_notsurvived_male = np.mean(df[(df['Sex'] == 'male') & (df['Survived'] == 0)]['Age'])


# Задание 35. Минимальная, максимальная и средняя стоимость билета
max_ticket_cost = np.nanmax(df['Fare'])
min_ticket_cost = np.nanmin(df['Fare'])
average_ticket_cost = np.nanmean(df['Fare'])


# Задание 36. Стандартное отклонение возраста
standard_age_deviation = np.nanstd(df['Age'])

# Контрольный вопрос
# По результатам анализа доля выживших женщин оказалась выше,
# чем мужчин. Также были рассчитаны различия в среднем возрасте
# мужчин и женщин, а также среди выживших и погибших.

# Таблица
# Результаты анализа с помощью NumPy
numpy_statistics = {
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
        standard_age_deviation
    ]
}

print('\nРезультаты анализа:')
print(pd.DataFrame(numpy_statistics))


# Часть 5
# Фильтрация данных

# Задание 1. Мужчины старше 30 лет, путешествовавшие первым классом
first_class_men_over_30 = (df['Sex'] == 'male') & (df['Age'] > 30) & (df['Pclass'] == 1)
print(f'\nКоличество мужчин старше 30 лет, путешествовавших первым классом: {np.sum(first_class_men_over_30)}')
print(df[first_class_men_over_30][:10])


# Задание 2. Пассажиры моложе 18 лет или женщины, которые при этом выжили
survived_women_or_minors = (df['Survived'] == 1) & ((df['Age'] < 18) | (df['Sex'] == 'female'))
print(f'\nКоличество пассажиров моложе 18 лет или женщин, которые при этом выжили: {np.sum(survived_women_or_minors)}')


# Задание 3. Пассажиры третьего класса, стоимость билета которых выше средней стоимости билета в этом классе
count_third_class_above_average_fare = np.sum(
    (df['Pclass'] == 3) & ((df['Fare']) > (np.nanmean(df[df['Pclass'] == 3]['Fare'])))
)
print(f'\nКоличество пассажиров третьего класса, стоимость билета которых выше средней стоимости билета в этом классе: {count_third_class_above_average_fare}')
print(df[(df['Pclass'] == 3) & ((df['Fare']) > (np.nanmean(df[df['Pclass'] == 3]['Fare'])))])

# Задание 4. Пассажиры от 20 до 40 лет включительно, отправившиеся из порта S
count_passengers_age_20_to_40_from_S = np.sum(
    ((df['Age'] >= 20) & (df['Age'] <= 40)) & (df['Embarked'] == 'S')
)
print(f'\nКоличество пассажиров от 20 до 40 лет включительно, отправившихся из порта S: {count_passengers_age_20_to_40_from_S}')
print(df[(df['Age'] >= 20) & (df['Age'] <= 40) & (df['Embarked'] == 'S')])

# Контрольный вопрос
# Логическое И (&) означает, что должны выполняться все условия.
# Логическое ИЛИ (|) означает, что достаточно выполнения хотя бы
# одного из условий.

# Часть 6

# Задание 37. Группировка по классу (Pclass) и полу (Sex)
passengers_by_class_and_sex = df.groupby(['Pclass', 'Sex'])

passenger_count_by_class_sex = passengers_by_class_and_sex.size()
print('\nКоличество пассажиров: ')
print(passenger_count_by_class_sex)


mean_age_by_class_sex = passengers_by_class_and_sex['Age'].mean()
print('\nСредний возраст пассажиров: ')
print(mean_age_by_class_sex)


mean_fare_by_class_sex = passengers_by_class_and_sex['Fare'].mean()
print('\nСредняя стоимость билета: ')
print(mean_fare_by_class_sex)


survival_rate_by_class_sex = passengers_by_class_and_sex['Survived'].mean() * 100
print('\nДоля выживших (%): ')
print(survival_rate_by_class_sex)


# Задание 38. Группировка по порту посадки (Embarked)
passengers_by_embarkation_port = df.groupby('Embarked')

passenger_count_by_port = passengers_by_embarkation_port.size()
print('\nКоличество пассажиров по портам посадки:')
print(passenger_count_by_port)


survival_rate_by_port = passengers_by_embarkation_port['Survived'].mean() * 100
print('\nПроцент выживших по портам посадки:')
print(survival_rate_by_port)


# Задание 39. Класс пассажиров с наибольшей долей выживших
passengers_by_class = df.groupby('Pclass')

highest_survival_rate = 0
for class_number, survival_rate in passengers_by_class['Survived'].mean().items():
    if survival_rate > highest_survival_rate:
        highest_survival_rate = survival_rate
        class_with_highest_survival_rate = class_number

print(f'\nНаибольшая доля выживших в классе {class_with_highest_survival_rate}: {highest_survival_rate * 100:.2f}')


# Часть 7

# Задание 40. Сохранение обработанного DataFrame
df.to_csv('titanic_processed.csv', index=False)


# Задание 41. Сохранение результатов группировки
print('\nСохранение результатов группировки в отдельный CSV-файл:')
titanic_statistics = {
    'Pclass': passenger_count_by_class_sex.index.get_level_values('Pclass'),
    'Sex': passenger_count_by_class_sex.index.get_level_values('Sex'),
    'Количество пассажиров': passenger_count_by_class_sex,
    'Средний возраст': mean_age_by_class_sex,
    'Доля выживших (%)': survival_rate_by_class_sex,
    'Средняя стоимость билета': mean_fare_by_class_sex
}

print(pd.DataFrame(titanic_statistics))

pd.DataFrame(titanic_statistics).to_csv('titanic_statistics.csv', index=False)


# Задание 42. Повторная загрузка и проверка обработанного CSV
print('\nПовторная загрузка обработанного файла и проверка корректности сохранения:')

processed_df = pd.read_csv('titanic_processed.csv')

print('\nПервые строки обработанной таблицы:')
print(processed_df.head())

print('\nРазмер обработанной таблицы:')
print(processed_df.shape)

print('\nНазвания столбцов:')
print(processed_df.columns)

print('\nКоличество пропусков:')
print(processed_df.isna().sum())

print('\nПроверка совпадения таблиц:')
print(processed_df.equals(df))

# Часть 8. Выводы по работе
print('\nЧасть 8. Выводы по работе')
# 43. Больше всего пропусков было в Cabin (327), затем в Age (86) и Fare (1).

# 44. Пропуски в Age заполнены медианой, Cabin удалён.
# Количество известных значений увеличилось с 332 до 418.
# Среднее и стандартное отклонение возраста изменились, а медиана, минимум и максимум остались прежними.
# Удаление строк с пустым Embarked не повлияло на размер таблицы, поскольку таких пропусков не было.
# Количество строк не изменилось, итоговый размер таблицы — 418 × 11.

# 45. Доля выживших женщин оказалась выше, чем мужчин.
print(f'\nПроцент выживших женщин: {female_percent:.2f}%')
print(f'Процент выживших мужчин: {male_percent:.2f}%')


# 46. Наибольшая доля выживших наблюдалась среди пассажиров первого класса (39 задание)
print(f'\nНаибольшая доля выживших наблюдалась в классе {class_with_highest_survival_rate}')


# 47. Pandas помог обрабатывать, фильтровать и группировать данные,
# а NumPy — выполнять математические вычисления и статистический анализ.

