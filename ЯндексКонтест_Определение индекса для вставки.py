# Массив отсортирован по возрастанию.
#
# На Земле учёным нужно определить, есть ли в массиве определённая концентрация
# марсия. Для этого им нужна программа, которая отыскивает в массиве
# заданную концентрацию — целевое значение.
#
# Если в массиве есть целевое значение, программа должна вернуть индекс первого
# такого элемента, в котором хранится это значение.
#
# Если целевого значения в массиве нет, программа должна вернуть индекс, под
# которым это значение могло бы располагаться в массиве.
#
# Таким образом, задача — найти индекс целевого значения в отсортированном
# массиве или определить индекс, на котором могло бы быть это значение.
#
# Напишите программу, которая принимает на вход массив и целевое значение,
# а возвращает индекс массива, где находится или должно находиться целевое значение.


# Формат ввода
# Первая строка — массив целых чисел через пробел.
#
# Вторая строка — искомое значение.
#
# Формат вывода
# Целое число: индекс искомого значения в существующем массиве, если оно
# там есть, или индекс, на котором это значение должно оказаться, если его нет в массиве.

# Пример 1
# Ввод
# 1 3 5 6
# 5

# Вывод
# 2

arr = list(map(int, input().split()))
num = int(input())
result = []
index = 0


def find_index(data, num):
    left_pointer = 0
    right_pointer = len(data) - 1
    # граничные значения
    if data[right_pointer] < num:
        return len(data)
    elif data[left_pointer] >= num:
        return 0

    while left_pointer <= right_pointer:
        mid = round(left_pointer + right_pointer) // 2  # индекс эл-та в центре
        if data[mid] == num:
            return mid
        if data[mid] < num:
            left_pointer = mid + 1
        else:
            right_pointer = mid - 1
            return right_pointer + 1
        #return mid + 1


if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    print(find_index(arr, num))
