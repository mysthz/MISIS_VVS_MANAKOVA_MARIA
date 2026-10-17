def summ(a, b):
    print(f'Результат {a+b}')
def substraction(a, b):
    print(f'Результат {a-b}')
def multiplication(a, b):
    print(f'Результат {a*b}')
def division(a, b):
    if b != 0:
        print(f'Результат {a/b}')
    else:
        print('На ноль делить нельзя')

a = float(input("Введите первое число: "))
oper = input("Введите операцию (+, -, *, /): ")
b = float(input("Введите второе число: "))

if oper == '+':
    summ(a, b)
elif oper == '-':
    substraction(a, b)
elif oper == '*':
    multiplication(a, b)
elif oper == '/':
    division(a, b)
else:
    print("Ошибка")