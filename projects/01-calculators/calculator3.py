def operations(a, b, operation):
    if operation == "+":
        print(f'Результат {a + b}')
    elif operation == "-":
        print(f'Результат {a - b}')
    elif operation == "*":
        print(f'Результат {a * b}')
    elif operation == "/":
        if b!=0:
            print(f'Результат {a / b}')
        else:
            print("На ноль делить нельзя")
while True:
    a = float(input("Введите первое число: "))
    oper = input("Введите операцию (+, -, *, /): ")
    b = float(input("Введите второе число: "))
    operations(a, b, oper)