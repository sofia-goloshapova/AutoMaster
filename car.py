class Car:
    """Класс Автомобиль"""

    def __init__(self, brand, model, year, license_plate, owner):
        self.brand = brand  # Марка
        self.model = model  # Модель
        self.year = year  # Год выпуска
        self.license_plate = license_plate  # Гос. номер
        self.owner = owner  # Владелец (объект Client)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year} г.), № {self.license_plate}"