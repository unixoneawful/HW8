# 1 Наследование
# object
#
# 2 плиморфизм

# 3 инкапсуляция
# _ = protected
# __ = скрытый

class Bank:
    def __init__(self, name, money, key):
        self.name = name
        self.__money = money
        self._key = key

    def __str__(self):
        return f'{self.name}:{self.__money}'

    def keys(self):
        self._printKey()

    def _printKey(self):
        print(self._key)


user = Bank('Мирлан', 9_000_000, '12edswadw')
user._Bank__money = 100000
# user.keys()
# user._key = '1234'
# user._printKey()
# user.keys()
# print(user._key)


print(user)
print(user.__dir__())
