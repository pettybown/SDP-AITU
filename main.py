from FahrenheitTemperature import FahrenheitTemperature
from CelsiusTemperature import CelsiusTemperature
from KelvinTemperature import KelvinTemperature
from TemperatureAdapter import TemperatureAdapter

fahrenheit_temp = FahrenheitTemperature()
celsius_temp = CelsiusTemperature(0)
kelvin_temp = KelvinTemperature(273)

adapter_temp = TemperatureAdapter(celsius_temp.temperature)
print(adapter_temp.get_temperature() + kelvin_temp.get_temperature() + fahrenheit_temp.get_temperature())
