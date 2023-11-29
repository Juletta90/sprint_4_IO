# В общем виде план решения будет такой:
#  - Получить все варианты маршрутов, охватывающих все нужные точки.
#  - Для каждого варианта посчитать общее расстояние.
#  - Сравнить длину маршрутов и выбрать кратчайший.

# У нас есть расстояния между нужными точками.

# запишем данные не в список, а в кортеж — в неизменяемую коллекцию!
# Так будет эффективнее! Кортежи потребуют меньше памяти.

# Каждый вложенный кортеж в distances соответствует элементу
# из places — из перечня мест, которые надо посетить:

places = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')

distances = (
    (0, 3570, 2230, 6430, 600),   # Расстояния от Gale.
    (3570, 0, 5280, 4530, 3315),  # Расстояния от Jezero.
    (2230, 5280, 0, 6715, 2540),  # Расстояния от Gusev.
    (6430, 4530, 6715, 0, 6400),  # Расстояния от Meridiani.
    (600, 3315, 2540, 6400, 0),   # Расстояния от Elysium.
)

# __________________Модуль itertools и генераторы______________
# Следующий шаг — составить все возможные маршруты,
# пролегающие через нужные точки.
# в Python, в модуле itertools, есть готовая функция,
# которая позволяет комбинировать любые последовательности объектов.

# Для решения нашей задачи потребуется функция permutations(),
# она возвращает итерируемый объект со всеми возможными комбинациями
# элементов заданной последовательности. Посмотрим на неё в деле:

from itertools import permutations

places = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')

# Получим все возможные комбинации элементов кортежа places...
combinations = permutations(places)
# ...и проитерируемся по объекту с этими комбинациями:
for travel_path in combinations:
    print(travel_path)

# Посмотрим, сколько получилось маршрутов и как они выглядят.
# Для этого применим функцию enumerate() — она получает на вход
# коллекцию и возвращает итерируемый объект — коллекцию кортежей;
# каждый кортеж состоит из двух элементов: индекса элемента и его значения.

# ...и проитерируемся по объекту с этими комбинациями:
for path_index, travel_path in enumerate(combinations):
    print(path_index, travel_path)

# Возьмём наугад любой из маршрутов и отработаем на нём
# вычисление общей длины маршрута:
# current_path = ('Gusev', 'Meridiani', 'Gale', 'Jezero', 'Elysium')

# Для любого маршрута потребуется четыре перемещения от точки к точке:
# movements = len(places) - 1.
# Создаём цикл с количеством итераций, равным количеству перемещений,
# и  попарно находим расстояния между точками:
# Gusev — Meridiani,
# Meridiani — Gale,
# Gale — Jezero,
# Jezero — Elysium.
# Из current_path получаем первое название и следующее за ним:

current_path = ('Gusev', 'Meridiani', 'Gale', 'Jezero', 'Elysium')
movements = len(places) - 1

for movement_index in range(movements):
    current_place = current_path[movement_index]
    next_place = current_path[movement_index + 1]

# На первой итерации цикла current_place — это 'Gusev',
# а next_place — это 'Meridiani'. Чтобы получить расстояние между ними, надо:
#  - В кортеже distances найти строку со всеми расстояниями от Gusev.
#  - В этой строке найти элемент, в котором записано расстояние
#    от Gusev до Meridiani.

# Для начала получим индексы элементов 'Gusev' и 'Meridiani' в кортеже places.
# Найти индекс элемента по его значению можно методом index():

    #current_place_index = places.index('Gusev')   # current_place_index = 2
    #next_place_index = places.index('Meridiani')  # next_place_index = 3

# Вместо строк подставим переменные current_place и next_place,
# ведь в цикле будут подставляться разные значения:

    current_place_index = places.index(current_place)
    next_place_index = places.index(next_place)

# Теперь в кортеже distances надо найти элемент, в котором записаны
# расстояния от Gusev до Meridiani
# (эти названия сейчас хранятся в current_place и next_place).

# Получаем кортеж, где хранятся все расстояния от Gusev до других точек:
gusev_distances = distances[current_place_index]  # (2230, 5280, 0, 6715, 2540)

# Расстояние от Gusev до Meridiani в этом кортеже указано под тем же индексом,
# под которым хранится значение Meridiani в кортеже places.
# Этот индекс записан в next_place_index:

# Из этого кортежа получаем расстояние Gusev - Meridiani:
gusev_meridiani_path = gusev_distances[next_place_index]  # 6715


# Получить расстояние от current_place до next_place можно одним выражением:

distance = distances[current_place_index][next_place_index]

# Обрабатываем один из маршрутов:
current_path = ('Gusev', 'Meridiani', 'Gale', 'Jezero', 'Elysium')

# Кортеж с названиями:
places = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')



#___________________-ИТОГО-_______________________________________-

# Расстояния между точками:
distances = (
    (0, 3570, 2230, 6430, 600),  # Расстояния от Gale.
    (3570, 0, 5280, 4530, 3315),  # Расстояния от Jezero.
    (2230, 5280, 0, 6715, 2540),  # Расстояния от Gusev.
    (6430, 4530, 6715, 0, 6400),  # Расстояния от Meridiani.
    (600, 3315, 2540, 6400, 0),  # Расстояния от Elysium.
)
# Количество перемещений между точками.
movements = len(places) - 1

# Общая длина пути: будем суммировать полученные расстояния
# для каждой пары current_place - next_place.
current_path_length = 0

# Для каждого перемещения от одной точки к другой:
for movement_index in range(movements):
    # Текущая точка.
    current_place = current_path[movement_index]
    # Следующая точка.
    next_place = current_path[movement_index + 1]
    # Индекс текущей точки в кортеже places:
    current_place_index = places.index(current_place)
    # Индекс следующей точки в кортеже places:
    next_place_index = places.index(next_place)
    # Расстояние между текущей и следующей точкой:
    distance = distances[current_place_index][next_place_index]
    # Добавляем расстояние между двумя точками к общему пути.
    current_path_length += distance

print(current_path_length)


#____________________--Поиск минимального значения--_____________________

# Мы написали код, вычисляющий протяжённость одного маршрута.
# А все маршруты собраны в итерируемый объект permutations(places),
# так что не составит труда перебрать их все:
# обрамляем наш код в ещё один цикл — и погнали!

# Кортеж с названиями:
places = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')

# Расстояния между точками:
distances = (
    (0, 3570, 2230, 6430, 600),
    (3570, 0, 5280, 4530, 3315),
    (2230, 5280, 0, 6715, 2540),
    (6430, 4530, 6715, 0, 6400),
    (600, 3315, 2540, 6400, 0),
)
# Количество перемещений между точками.
movements = len(places) - 1

# Цикл, перебирающий все возможные маршруты:
for current_path in permutations(places):
    current_path_length = 0
    # Цикл, вычисляющий расстояние для отдельного маршрута:
    for movement_index in range(movements):
        ...

# Внешний цикл будет перебирать все маршруты и вычислять протяжённость
# каждого из них. Остаётся выбрать наименьшее значение из всех полученных;
# обозначим его переменной min_path_length.

# Решить эту задачу можно двумя способами:
#  - Сохранять все расстояния в массив, а в самом конце работы программы
#    найти в этом массиве минимальное значение при помощи функции min().
#  - На каждом шаге сравнивать текущий результат current_path_length с
#    имеющимся min_path_length при помощи функции min() и
#    меньшее значение сохранять в min_path_length:

# min_path_length = min(current_path_length, min_path_length)

# в качестве стартового значения для min_path_length можно задать число,
# заведомо большее всех возможных.

# Из модуля sys можно импортировать константу maxsize — она хранит число,
# определяющее технические пределы для некоторых вычислений: например, длина
# последовательности не может быть больше, чем maxsize.
# Для 32-битных операционных систем значение maxsize равно 2147483647
# а для 64-битных систем — 9223372036854775807.

# Если перед выполнением внешнего цикла присвоить переменной
# min_path_length значение maxsize, то на первой итерации цикла
# выражение min_path_length = min(current_path_length, min_path_length)
# отработает без ошибок!

# from sys import maxsize
#
# min_path_length = maxsize
#
# for current_path in permutations(places):
#     current_path_length = ... # Здесь считаем длину маршрута.
#     min_path_length = min(current_path_length, min_path_length)


#_______________ИТОГО____________________________-

from itertools import permutations
from sys import maxsize


def travel_salesman_problem(places, distances):
    movements = len(places) - 1
    # Вводим переменную для хранения самого короткого маршрута.
    min_path = None
    min_path_length = maxsize
    for current_path in permutations(places):
        current_path_length = 0
        for movement_index in range(movements):
            current_place = current_path[movement_index]
            next_place = current_path[movement_index + 1]
            current_place_index = places.index(current_place)
            next_place_index = places.index(next_place)
            distance = distances[current_place_index][next_place_index]
            current_path_length += distance
        # Если полученное расстояние меньше самого короткого пути...
        if current_path_length < min_path_length:
            # ...назначаем полученное расстояние самым коротким.
            min_path_length = current_path_length
            # Запоминаем самый короткий маршрут.
            min_path = current_path
    # Вместо одного значения возвращаем кортеж с двумя значениями:
    # расстоянием и самым коротким маршрутом.
    return min_path_length, min_path


if __name__ == '__main__':
    places_example = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')
    distances_example = (
        (0, 3570, 2230, 6430, 600),
        (3570, 0, 5280, 4530, 3315),
        (2230, 5280, 0, 6715, 2540),
        (6430, 4530, 6715, 0, 6400),
        (600, 3315, 2540, 6400, 0),
    )
    min_path_length_example, min_path_example = travel_salesman_problem(
        places_example, distances_example
    )
    print(min_path_length_example, min_path_example)













