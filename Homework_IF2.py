a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a > b and a < c or a > c and a < b:
    print("Срединным является первое число: ", a)
elif b > a and b < c or b > c and b < c:
    print("Срединным является второе число: ", b)
elif c > a and c < b or c > b and c < a:
    print("Срединным является третье число: ", c)
else:
    print("Cреди введенных чисел есть равные")
