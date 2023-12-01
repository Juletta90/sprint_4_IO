# # Установим стартовые условия:
# левый индекс = 0
# правый индекс = последнему индексу в исходном массиве
#
# while левый индекс меньше правого или равен ему:
#   найти индекс среднего элемента
#   сравнить значение этого элемента с искомым
#   если значения совпадают, вернуть результат
#   if искомое больше найденного элемента
#     изменить левый индекс, чтобы от исходного массива осталась только правая половина
#   if искомое меньше найденного элемента
#     изменить правый индекс, чтобы от исходного массива осталась только левая половина

#wins = [1223125, 2128437, 2128500, 2741001, 4567687, 4567890, 7495938, 9314543]
#my_ticket = 4567890

wins = [3, 7, 10, 20, 23]
my_ticket = 23

def find_element(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    # Левая граница (левый индекс) рассматриваемого набора элементов.
    # В начале работы она равна индексу первого элемента в списке - нулю.
    left = 0
    # Правая граница (правый индекс) рассматриваемого набора элементов.
    # В начале работы она равна индексу последнего элемента в списке.
    right = len(sorted_numbers) - 1
    # Пока левая граница меньше правой или равна ей:
    while left <= right:
        # Находим в наборе элементов индекс среднего элемента.
        mid = (left + right) // 2
        # Если элемент с этим индексом равен искомому, возвращаем его индекс.
        if sorted_numbers[mid] == element:
            return mid
        # Если средний элемент меньше искомого...
        if sorted_numbers[mid] < element:
            # ...то изменяем левую границу поиска:
            left = mid + 1
        # Если средний элемент больше искомого...
        else:
            # ...то изменяем правую границу поиска:
            right = mid - 1
    # Если левая граница оказалась больше правой,
    # значит, элемент не найден. Возвращаем None.
    return None


print(find_element(wins, my_ticket))

