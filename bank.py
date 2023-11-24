# Іноді ви можете використати property() для створення
# доступу до атрибутів через геттери та сеттери для
# забезпечення певних перевірок або операцій перед
# отриманням або зміною атрибутів. Створіть клас для
# роботи з банківським рахунком, щоб гроші знялися або
# зарахувалися тільки при виконанні певних умов
# (наприклад, якщо гроші на рахунку є).

class BankAccount:
    __balance = 0

    def __init__(self, name) -> None:
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def balance(self):
        return self.__balance

    def deposit(self, value):
        if isinstance(value, (int, float)):
            if value > 0: 
               self.__balance += value
            else:
               raise ValueError("value can not be negative or 0")
        else:
            raise ValueError("value must be a number")
    
    def withdraw(self, value):
        if isinstance(value, (int, float)):
            if value > 0:
                if self.__balance - value >= 0: 
                    self.__balance -= value
                else:
                    raise ValueError("Not enough balance")
            else:
               raise ValueError("value can not be negative or 0")
        else:
            raise ValueError("value must be a number")

acc = BankAccount('Bobby')
acc.deposit(100)
acc.withdraw(10)
print(acc.balance)