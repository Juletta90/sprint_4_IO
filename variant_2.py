# Есть и ещё один вариант:
# результаты сложения, полученные на каждой итерации, добавлять в массив output_numbers;
# напечатать распакованный массив, разделив элементы символами перевода строки.
# Чтобы распаковать список на отдельные элементы, перед именем списка указывается звёздочка:

import sys


def main():
    num_lines = int(sys.stdin.readline().rstrip())  # нужно самому ввести данные # 3
                                                                                 # 5 6
                                                                                 # 7 8
                                                                                 # 9 10
    output_numbers = [None] * num_lines
    for i in range(num_lines):
        line = sys.stdin.readline().rstrip()
        first, second = line.split()
        first = int(first)
        second = int(second)
        # Записываем результат в массив без преобразования в строку.
        output_numbers[i] = first + second
    # В конце печатаем распакованный список,
    # добавляя между значениями символы перевода строки.
    print(*output_numbers, sep='\n')


if __name__ == '__main__':
    main()

