def digit_root(num):
    while num > 10:
        sum = 0
        for i in str(num):
            sum += int(i)
        num = sum
    return num


print('Введите число для расчета цифрового корня:')
x = input()
if 0 < int(x) <= 10**7 and isinstance(int(x), int):
    print(digit_root(int(x)))
else:
    print('Введено число, которое не соответствует условиям')
