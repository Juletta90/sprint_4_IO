# Поменять местами значения двух элементов
# Два элемента списка могут обменяться значениями,
# например, при посредстве дополнительной переменной:

#_______________________1 способ:________________________
# Исходный список.
data = ['Белка', 'Стрелка']

# Распечатываем содержимое элементов с индексами 0 и 1.
print(data[0], data[1])
# Белка Стрелка

# Сохраняем значение элемента с индексом 0 во временную переменную temp.
temp = data[0]
print(temp)
# Белка

# Присваиваем элементу с индексом 0 значение элемента с индексом 1.
data[0] = data[1]
print(data[0], data[1])
# Стрелка Стрелка
# Оба элемента имеют одинаковое значение - Стрелка.

# Присваиваем элементу с индексом 1 значение временной переменной temp.
data[1] = temp
print(data[0], data[1])
print()
# Стрелка Белка
# Значения элементов «поменялись» местами.



#_______________________2 способ:________________________

data = ['Белка', 'Стрелка']
# Обмениваем значения элементов с помощью одной строки:
data[0], data[1] = data[1], data[0]  # Это же два кортежа, просто без скобок!

# Проверим, что значения элементов поменялись местами.
print(data)
print()
# ['Стрелка', 'Белка']


# Этот способ проще и лаконичнее, чем вариант с дополнительной переменной, —
# будем применять именно его. Чтобы понять, как он работает,
# надо вспомнить про кортежи и их распаковку.

# При создании кортежа он может быть записан как со скобками,
# так и без скобок (если в нём более одного элемента):

dog_1 = 'Белка'
dog_2 = 'Стрелка'

# Создаём кортеж из двух элементов. Для объявления кортежа
# скобки не обязательны, обойдёмся без них:
without_parentheses = dog_1, dog_2

# Создаём кортеж из двух элементов со скобками.
with_parentheses = (dog_1, dog_2)

# Проверяем, что кортежи равны между собой.
print(without_parentheses == with_parentheses)
# True

# Проверяем, что это действительно кортежи.
print(type(without_parentheses), type(with_parentheses))
print()
# <class 'tuple'> <class 'tuple'>

#_______________________________________________________

# Идём дальше: любой кортеж или список можно распаковать
# на несколько переменных.

data = ('Белка', 'Стрелка')
# Распаковываем содержимое кортежа - присваиваем переменным значения элементов кортежа.
dog_1, dog_2 = data

# Печатаем значения переменных.
print(dog_1, dog_2)
print()
# Белка Стрелка

# В строке dog_1, dog_2 = data и слева, и справа от знака «равно»
# стоят кортежи. Кортеж dog_1, dog_2 создаётся из кортежа data.
# В итоге:

# Выражение, в котором переменные обмениваются значениями:
dog_1, dog_2 = dog_2, dog_1
# ...полностью эквивалентно выражению, записанному с использованием скобок:
(dog_1, dog_2) = (dog_2, dog_1)

#_____________________________________________________________________
# И в том, и в другом случае кортеж в левой части равенства создаётся
# за счёт распаковки кортежа из правой части.
# Таким образом, чтобы обменять значения переменных друг с другом,
# слева и справа от знака равенства указывают переменные, но в разном порядке.
#
# Переменные слева от знака равенства примут значения соответствующих
# переменных, стоящих справа от знака равенства:
#____________________________________________________________________



# Этим же способом можно обменять значения двух элементов в списке:
data = ['Белка', 'Стрелка']

# Элементы списка обмениваются значениями.
data[0], data[1] = data[1], data[0]
print(data[0], data[1])
print()
# Стрелка Белка
# Значения элементов поменялись местами.