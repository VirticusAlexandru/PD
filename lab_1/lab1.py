x = int(input("Введите число от 1 до 9: "))

if 1 <= x <= 3:
    s = input("Введите строку: ")
    n = int(input("Введите количество повторов строки: "))
    for i in range(n):
        print(s)

elif 4 <= x <= 6:
    m = int(input("Введите степень, в которую нужно возвести число: "))
    result = x ** m
    print("Результат:", result)

elif 7 <= x <= 9:
    for i in range(1, 11):
        x += 1
        print(x)

else:
    print("Ошибка ввода")
