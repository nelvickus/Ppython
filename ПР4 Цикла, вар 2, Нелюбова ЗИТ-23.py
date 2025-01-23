
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

if A < B:
    for number in range(A, B + 1):
        print(number, end=' ')
else:
    for number in range(A, B - 1, -1):
        print(number, end=' ')
