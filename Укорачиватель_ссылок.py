# Реализуйте класс MarsURLEncoder.
# В конструкторе класса __init__(...) создайте атрибут — хранилище ссылок.
# Это должен быть словарь, в котором каждому случайно сгенерированному
# ключу соответствует длинная ссылка. Если для ссылки
# https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html создан хеш X7NYIol,
# то в словарь должен быть добавлен такой элемент:

# {
#     ...,
#     'X7NYIol': 'https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'
# }

# В классе должно быть два метода:
#  - метод encode() должен получать на вход длинные ссылки и возвращать короткие;
#  - метод decode() должен принимать короткую ссылку и возвращать исходную, длинную.
# К изменяющейся части короткой ссылки особых требований нет — там может
# быть написана любая последовательность букв и цифр.
# Важно, чтобы по короткой ссылке можно было восстановить длинную.

import hashlib


class MarsURLEncoder:

    def __init__(self):
        self.url_dict = {}
        self.prefix = 'https://ma.rs/'

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        # получениe хеша в виде шестнадцатеричной строки - метод hexdigest().
        # Если нужно принять какой-то ввод с консоли и хешировать его,
        # не забудьте закодировать строку в последовательности байтов:
        # encode() - Предположительно по умолчанию UTF-8
        hash_object = hashlib.sha1(long_url.encode()).hexdigest()
        self.url_dict[hash_object] = long_url  # добавление в словарь
        return self.prefix + hash_object

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.url_dict.get(short_url)  # обращение к ключу словаря




#_______________________2Й ВАРИАНТ_________________________________

# тут реализована проверка на уникальность полученного хеша —
# не случилась ли коллизия. Если полученный хеш уже использован в словаре,
# то нужно сгенерировать хеш заново:
# вероятность повторной коллизии довольно мала.


class MarsURLEncoder2:

    def __init__(self):
        self.dict = {}

    def encode(self, long_url):
        header = "https://ma.rs/"
        key = header + hashlib.sha3_384(long_url.encode()).hexdigest()
        if self.dict.get(key) is None:  # проверка на коллизии
            self.dict[key] = long_url
        return key

    def decode(self, short_url):
        return self.dict.get(short_url)




import hashlib

class MarsURLEncoder:

    def __init__(self):
        self.dict = {}

    def encode(self, long_url):
        heder = "https://ma.rs/"
        key = heder+hashlib.sha3_384(long_url.encode()).hexdigest()
        if self.dict.get(key) is None:
            self.dict[key] = long_url
        return key

    def decode(self, short_url):
        return self.dict.get(short_url)






# # список доступных алгоритмов
# print(hashlib.algorithms_available)
#
# hash_object = hashlib.md5(b'Hello World')
# print(hash_object.hexdigest())



# https://python-scripts.com/md5-sha1

# import hashlib
#
# mystring = input('Enter String to hash: ')
#
# # Предположительно по умолчанию UTF-8
# hash_object = hashlib.md5(mystring.encode())
# print(hash_object.hexdigest())
