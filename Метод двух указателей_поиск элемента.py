# Заданы число и отсортированный список из целых чисел.
# Напишите функцию, которая найдёт в этом списке два элемента,
# сумма которых равна заданному числу, и вернёт кортеж с индексами этих элементов.
#
# Нельзя использовать один и тот же элемент дважды.
# Если при определённых входных данных решения у задачи нет,
# функция должна вернуть None.

# Например:
# задано число 10;
# задан список [1, 2, 3, 4, 5, 6, 7, 11].

# Сумму 10 дают элементы со значениями 3 и 7 (их индексы — 2 и 6) и
# элементы со значениями 4 и 6 (их индексы — 3 и 5).
# Функция должна вернуть кортеж с любой из этих пар индексов: (2, 6) или (3, 5).

# Ответ (4, 4) принят не будет: две пятёрки в сумме действительно дают 10,
# но дважды использовать один элемент нельзя.

# Наивным решением «в лоб» будет перебрать последовательно все элементы,
# сложив каждый с каждым в надежде, что у задачи есть решение.
# Временная сложность такого решения — квадратичная.

#______________________1 ВАРИАНТ_____________________________
def find_two_indexes(data, expected_sum):

    # запускаем первый цикл
    for i in range(len(data) - 1):
        #  запускаем второй цикл
        for j in range(i + 1, len(data)):
            # если получили нужный результат —
            if expected_sum == data[i] + data[j]:
                return i, j


#______________________2 ВАРИАНТ_________________________________

def find_two_indexes_2(data, expected_sum):
    # Для первого индекса и первого слагаемого.
    for first_index, first_value in enumerate(data):
        # Для второго индекса и второго слагаемого.
        for second_index, second_value in enumerate(data):
            # Если индексы равны, то есть это один и тот же элемент...
            if first_index == second_index:
                # ...переходим к следующему элементу.
                continue
            # Если сумма значений равна ожидаемому результату...
            if first_value + second_value == expected_sum:
                # ...вернуть индексы элементов.
                return first_index, second_index


#_________________Метод двух указателей______________________

# Один из способов, позволяющих отбрасывать заведомо неподходящие варианты,
# — это метод двух указателей. Он применяется в ситуациях, когда данные
# хранятся в отсортированном массиве и необходимо найти в этом массиве
# значения, отвечающие определённым условиям, — например, заданную сумму
# двух элементов, как в приведённой задаче. Тем же методом можно найти,
# например, срез массива, где сумма значений будет равна заданному числу.

# Для работы создаются два указателя: левый left_pointer и правый right_pointer.
# Каждый из указателей «наведён» на определённый элемент массива — хранит
# индекс этого элемента. В самом начале работы указатель left_pointer
# указывает на первый элемент массива, а right_pointer — на последний.

# Алгоритм выполняется пошагово:
#  - Установили указатели на определённые индексы.
#  - Сравнили сумму значений элементов, на которые смотрят указатели.
#  - В зависимости от результатов сравнения сдвинули один из указателей на один элемент ближе к середине массива.
#  - Повторили все операции.

# В ходе работы индекс левого указателя может только увеличиваться, а
# индекс правого — только уменьшаться; указатели смещаются навстречу
# друг другу, к середине массива.
# Отрезок массива, «зажатый» между указателями, с каждым шагом уменьшается.
# Значения, оказавшиеся вне этого отрезка, признаются «бесперспективными», ]
# отбрасываются


def find_two_indexes_3(data, expected_result):
    # В начале работы
    # - левый указатель указывает на первый элемент списка (с индексом 0):
    left_pointer = 0
    # - правый указатель указывает на последний элемент списка.
    # Индекс этого элемента на единицу меньше длины списка.
    right_pointer = len(data) - 1
    # Пока индекс левого указателя меньше индекса правого указателя.
    while left_pointer < right_pointer:
        # Считаем сумму двух элементов.
        sum = data[left_pointer] + data[right_pointer]
        # Если она совпадает с искомой...
        if sum == expected_result:
            # ...возвращаем ответ:
            return left_pointer, right_pointer
        # Если сумма больше искомой, то...
        elif sum > expected_result:
            # ...надо уменьшить сумму: уменьшаем значение правого указателя.
            right_pointer -= 1
        # Все остальные варианты относятся к случаям, когда сумма меньше искомой.
        else:
            # Сумму надо увеличить, для этого увеличиваем значение левого указателя.
            left_pointer += 1

# В этом решении применён цикл while, а не for: ведь количество необходимых
# шагов заранее неизвестно, но зато известны два возможных условия выхода из цикла:
# когда найдётся искомое число,
# или когда указатели встретятся.

# За одну итерацию цикла сдвигается только один указатель, значит,
# указатели никак не смогут «разминуться» друг с другом или
# перескочить один через другой.
# Временная сложность такого решения задачи — линейная, а не квадратичная,
# как было в случае наивного решения. Никаких новых объектов при таком
# решении не создаётся — следовательно, нет и дополнительного расхода памяти.


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes_2(data, expected_sum))


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_result = 10
    print(find_two_indexes_3(data, expected_result))

