class Service:
    """Класс Услуга/Работа"""

    def __init__(self, name, price):
        self.name = name  # Название услуги
        self.price = price  # Стоимость

    def __str__(self):
        return f"{self.name} — {self.price} руб."