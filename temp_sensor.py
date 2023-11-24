# Створіть клас температурного датчика, де обмежується
# температура в межах прийнятних для датчика значень, за
# допомогою property().

class TemperatureSensor():
    __min_temp = -50
    __max_temp = 50

    def __init__(self) -> None:
        self._temperature = 0
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number")
        if TemperatureSensor.__min_temp < value < TemperatureSensor.__max_temp:
            self._temperature = value
        else: raise ValueError("Value can be in range -50, 50")

temp = TemperatureSensor()
temp.temperature = 25
print(temp.temperature)