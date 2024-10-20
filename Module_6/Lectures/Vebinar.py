# Базовый класс для всех устройств
class Device:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"{self.name} is now ON")

    def turn_off(self):
        print(f"{self.name} is now OFF")

# Миксин для устройств с регулировкой громкости
class VolumeControlMixin:
    def __init__(self):
        self.volume = 50  # уровень громкости по умолчанию

    def set_volume(self, level):
        self.volume = level
        print(f"Volume set to {self.volume}")

# Миксин для устройств с регулировкой яркости
class BrightnessControlMixin:
    def __init__(self):
        self.brightness = 70  # уровень яркости по умолчанию

    def set_brightness(self, level):
        self.brightness = level
        print(f"Brightness set to {self.brightness}")

# Класс телевизора с ЯВНЫМИ вызовами конструкторов
class SmartTV(Device, VolumeControlMixin, BrightnessControlMixin):
    def __init__(self, name):
        Device.__init__(self, name)  # Явный вызов конструктора Device
        VolumeControlMixin.__init__(self)  # Явный вызов конструктора VolumeControlMixin
        BrightnessControlMixin.__init__(self)  # Явный вызов конструктора BrightnessControlMixin

# Класс умной лампы с использованием super()
class SmartLamp(Device, BrightnessControlMixin):
    def __init__(self, name):
        super().__init__(name)  # Использование super() для вызова всех родительских классов
        # Дополнительная инициализация, если требуется

# Пример использования
print("=== SmartTV (явные вызовы конструкторов) ===")
tv = SmartTV("Living Room TV")
tv.turn_on()
tv.set_volume(30)
tv.set_brightness(80)

print("\n=== SmartLamp (использование super()) ===")
lamp = SmartLamp("Bedroom Lamp")
lamp.turn_on()
lamp.set_brightness(50)
lamp.turn_off()

class Weather:
    def __init__(self):
        pass


class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        print(f"Город с координатами: ({self.latitude}, {self.longitude})")


class City(Location):
    def __init__(self, name, temperatures, latitude, longitude):
        Location.__init__(self, latitude, longitude)
        self.name = name
        self.__temperatures = temperatures  # private
        print(f"{self.name} создан!")

    def average_temperature(self):
        return sum(self.__temperatures) / len(self.__temperatures)

    def get_temperatures(self):
        return self.__temperatures

    def set_temperatures(self, new_temperatures):
        """Устанавливает новый список температур."""
        if all(isinstance(t, (int, float)) for t in new_temperatures):
            self.__temperatures = new_temperatures
        else:
            print("Error: All temperature values must be numbers.")

    def display_info(self):
        """Выводит основную информацию о городе."""
        print(f"Город: {self.name}")
        print(f"Средняя температура за неделю: {self.average_temperature():.2f}°C")


class CoastalCity(City):
    def __init__(self, name, temperatures, humidity_levels, latitude, longitude):
        City.__init__(self, name, temperatures, latitude, longitude)
        self.__humidity_levels = humidity_levels
        print(f"Создан прибрежный город {self.name}!")

    def average_humidity(self):
        return sum(self.__humidity_levels) / len(self.__humidity_levels)

    def get_humidity_levels(self):
        return self.__humidity_levels

    def set_humidity_levels(self, new_humidity_levels):
        """Устанавливает новый список уровней влажности."""
        if all(isinstance(h, (int, float)) and 0 <= h <= 100 for h in new_humidity_levels):
            self.__humidity_levels = new_humidity_levels
        else:
            print("Ошибка: Все значения влажности должны быть числами от 0 до 100.")

    def display_info(self):
        """Выводит информацию о городе, включая среднюю влажность."""
        super().display_info()
        print(f"Average humidity: {self.average_humidity():.2f}%")


class MountainCity(City):
    def __init__(self, name, temperatures, elevation, latitude, longitude):
        super().__init__(name, temperatures, latitude, longitude)  # Использование super()
        self.__elevation = elevation
        print(f"Создан горный город {self.name}!")

    def get_elevation(self):
        return self.__elevation

    def set_elevation(self, new_elevation):
        """Устанавливает новую высоту города."""
        if isinstance(new_elevation, (int, float)) and new_elevation > 0:
            self.__elevation = new_elevation
        else:
            print("Ошибка: Высота должна быть положительным числом.")

    def display_info(self):
        """Выводит информацию о городе, включая высоту."""
        super().display_info()
        print(f"Высота над уровнем моря: {self.get_elevation()} м")


city1 = CoastalCity("Сочи", [22, 23, 24, 25, 26], [60, 65, 70, 75], 43.5855, 39.7231)
city2 = MountainCity("Нальчик", [-5, -6, -3, -2, -1], 5642, 43.3498, 42.4457)

print(city1.average_temperature())  # Средняя температура в Сочи
print(city1.get_humidity_levels())  # Влажность в Сочи
print(city2.get_elevation())  # Высота Эльбруса