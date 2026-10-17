a = input('Choose level (1/2/3/4/5) ')

if a == '1':
    methods = {
        'upper': str.upper,
        'lower': str.lower,
        'capitalize': str.capitalize,
    }
    print("upper - все в верхний регистр\n"
          "lower - все в нижний регистр\n"
          "capitalize - первая заглавная\n")
    c = input("Choose the method (upper / lower / capitalize): ").strip().lower()

    if c in methods:
        print(methods[c]('пРиВет МИР'))

        b = input("Write the stroke ")
        print(methods[c](b))

elif a =='2':
    methods = {
        'find': str.find,
        'replace': str.replace,
        'count': str.count,
    }
    print("methods:\n"
          "find - найти позицию первого входения подстроки\n"
          "replace - заменить все символы 'a' на символы 'б'\n"
          "count - посчитать количество элементов в строке")
    c = input("Choose the method: (find / replace / count): ").strip().lower()
    if c in methods:
        if c == 'find':
            print(f'Позиция первого входа подстроки "круто" - {methods[c]('Ботать это круто, очень круто', 'круто')}')
            b = input("Write the stroke ")
            b1 = input("Введите подстроку ")
            print(methods[c](b, b1))
        elif c == 'replace':
            print(f'Замена подстроки "круто" на "супер" - {methods[c]('Ботать это круто, очень круто', "круто", 'супер')}')
            b = input("Write the stroke ")
            b1 = input("Введите подстроку ")
            b2 = input('На какую подстроку заменить? ')
            print(methods[c](b, b1, b2))
        elif c == 'count':
            print(f'Количество букв "О" - {methods[c]('Ботать это круто, очень круто', "о")}')
            b = input("Write the stroke ")
            b1 = input("Введите подстроку ")
            print(methods[c](b, b1))

elif a == '3':
    methods = {
        'split': str.split,
        'join': str.join,
    }
    print("methods: "
          "split - разделить подстроки по введеному элементу-разделителю на элементы массива\n"
          "join - соединить элементы массива в строку по введеному элементу-разделителю. Нужно ввести, по какому элементу разделить строку и на какой элемент заменить")
    c = input("Choose the method: (split / join) ").strip().lower()

    if c in methods:
        if c == 'join':
            print(f'Преобразование строки "1, 2, 3, 4" в массив [1, 2, 3, 4] (деление по запятой), а потом в строку по разделителю "-" - {methods[c]("-", "1, 2, 3, 4".split(", "))}')
            b = input("Write the stroke ")
            s = input('Введите, по какому разделителю делить строку (пробел написать буквами): ')
            if s.lower() == 'пробел':
                s = ' '
            s1 = input('Введите новый элемент разделитель (пробел написать буквами): ')
            if s1.lower() == 'пробел':
                s1 = ' '
            print(methods[c](s1, b.split(s)))

        elif c == "split":
            print(f'Преобразование строки "1, 2, 3, 4" в массив [1, 2, 3, 4] по разделителю-запятой - {methods[c]("1, 2, 3, 4", ", ")}')
            b = input("Write the stroke ")
            s = input('Введите, по какому разделителю делить строку (пробел написать буквами): ')
            if s.lower() == 'пробел':
                s = ' '
            print(methods[c](b, s))

elif a == '4':
    methods = {
        'isdigit': str.isdigit,
        'isalpha': str.isalpha,
        'strip': str.strip,
    }
    tests = {
        'isdigit': ('1234*&%$',    'состоит ли строка "1234*&%$" только из цифр'),
        'isalpha': ('1234*&%$',    'состоит ли строка "1234*&%$" только из букв'),
        'strip':   ('  abc1234  ', 'строка "  abc1234  " без пробелов по краям'),
    }

    print("methods:\n"
          "isdigit - булевое значение, состоит ли строка только из цифр\n"
          "isalpha - булевое значение, состоит ли строка только из букв\n"
          "strip - убрать пробелы в начале и в конце строки")
    c = input("Choose the method (isdigit / isalpha / strip): ").strip().lower()

    if c in methods:
        test, text = tests[c]
        print(f"{text} - {methods[c](test)!r}")

        b = input("Write the stroke ")
        print(repr(methods[c](b)))

elif a == '5':
    def normalize(s):
        s = s.strip().strip(':')
        s = ' '.join(s.split(':'))
        return s.capitalize()

    print("Приведение строки к нормальному виду:\n")
    test = "      pYtHon:is:AWESome:      "
    print(f'Тест: "{test}" -> "{normalize(test)}"')





