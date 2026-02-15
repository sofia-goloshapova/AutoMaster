class Client:
    """Класс Клиент автомастерской"""

    def __init__(self, full_name, phone):
        self.full_name = full_name  # ФИО клиента
        self.phone = phone  # Номер телефона

    def __str__(self):
        return f"{self.full_name} (тел: {self.phone})"