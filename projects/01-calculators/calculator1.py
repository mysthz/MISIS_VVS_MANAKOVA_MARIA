a = float(input("Введите первое число: "))
oper = input("Введите операцию (+, -, *, /): ")
b = float(input("Введите второе число: "))

if oper == '+':
    res = a+b
    print(f'Результат {res}')
elif oper == '-':
    res = a-b
    print(f'Результат {res}')
elif oper == '*':
    res = a*b
    print(f'Результат {res}')
elif oper == '/':
    if b != 0:
        res = a/b
        print(f'Результат {res}')
    else:
        print('На ноль делить нельзя')
else:
    print("Ошибка")
