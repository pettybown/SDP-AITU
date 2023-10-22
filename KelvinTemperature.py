from Temperature import Temperature


class KelvinTemperature(Temperature):
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature
