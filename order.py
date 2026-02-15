class Order:
    """Класс Заказ на ремонт"""
    STATUSES = ["Принят", "В работе", "Готов", "Выдан"]

    def __init__(self, order_id, car, service, date):
        self.order_id = order_id  # Номер заказа
        self.car = car  # Автомобиль
        self.service = service  # Услуга
        self.date = date  # Дата приёма
        self.status = self.STATUSES[0]  # Текущий статус

    def set_status(self, new_status):
        """Изменить статус заказа"""
        if new_status in self.STATUSES:
            self.status = new_status
            return True
        return False

    def __str__(self):
        return (f"Заказ №{self.order_id} от {self.date}\n"
                f"Авто: {self.car}\n"
                f"Владелец: {self.car.owner}\n"
                f"Услуга: {self.service}\n"
                f"Статус: {self.status}")