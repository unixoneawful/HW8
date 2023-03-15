class Calculator:




    def __add__(self, num1, num2):

        return num1 + num2




    def __sub__(self, num1, num2):

        return num1 - num2




    def __mul__(self, num1, num2):

        return num1 * num2




    def __truediv__(self, num1, num2):

        return num1 / num2







cal = Calculator()




print(cal.__sub__(34, 23))

print(cal.__mul__(5, 32))

print(cal.__truediv__(33, 11))

print(cal.__add__(345, 54))

class Bank:

    def __init__(self,name , balance):

        self._name = name

        self._balance = balance

    def moneyX(self):

        try:

            money = int(input('Введите сумму для пополнения: '))

            return self._balance + money

        except ValueError:

            return 'Вводите только числа!'

    def _kill(self):

        kill_balanse = self._balance = 0

        return f'Ваш баланс: {kill_balanse}'

    def __jackpot(self):

        return f'Вы выиграли ДЖЕКПОООТ! {self._balance * 10}'

    def _stolenone(self, other):

        return f'Ваш баланс: {self._balance + other._balance}'

Beka = Bank('Bek', 1234)

Alim = Bank("Beka", 12345)

#print(Alim._kill())

# print(Alim.moneyX())

print(Alim._Bank__jackpot())

print(Alim._stolenone(Beka))
