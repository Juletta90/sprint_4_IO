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
        self.url_dict[hash_object] = long_url
        return self.prefix + hash_object

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        url_decode = hash_object.replace(long_url)
        pass






# список доступных алгоритмов
print(hashlib.algorithms_available)

hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())




# https://python-scripts.com/md5-sha1

# import hashlib
#
# mystring = input('Enter String to hash: ')
#
# # Предположительно по умолчанию UTF-8
# hash_object = hashlib.md5(mystring.encode())
# print(hash_object.hexdigest())