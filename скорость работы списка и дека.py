# Импорт библиотеки для работы с временем.
import time
# Импорт дека.
from collections import deque

# Количество элементов в списке и в деке.
elements_count = 100000

# Засекаем время начала.
start_time = time.time()
# Сначала проверяем обычный список.
data1 = []
for data_index in range(elements_count):
    # Каждый раз вставляем элемент в начало списка.
    data1.insert(0, f'Элемент номер {data_index}')
# Печатаем время выполнения для списка.
print(time.time() - start_time)

# Засекаем новое время для дека.
start_time = time.time()
# Создаём дек.
data2 = deque()
for data_index in range(elements_count):
    # Добавляем новые элементы в начало очереди.
    data2.appendleft(f'Элемент номер {data_index}')
# Печатаем время выполнения для дека.
print(time.time() - start_time)




# Для ограничения размера очереди при инициализации дека
# надо указать параметр maxlen.

data = deque(maxlen=10)

for item in range(15):
    data.appendleft(item)

print(data)

# Элементы от 0 до 4 включительно, первыми добавленные в очередь,
# были вытеснены из дека при добавлении последних элементов.

