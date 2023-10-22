from Temperature import Temperature


class CelsiusTemperature(Temperature):
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return str(self.temperature)
