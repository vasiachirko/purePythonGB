"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
"""
cubes = []
for i in range(1, 1001):
    cubes.append(i ** 3)

result = 0
for i in cubes:
    if sum(map(int, list(str(i)))) % 17 == 0:
        result += i

result2 = 0
for i in cubes:
    i += 17
    if sum(map(int, list(str(i)))) % 7 == 0:
        result2 += i
print(result)
print(result2)