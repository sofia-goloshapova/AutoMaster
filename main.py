from client import Client
from car import Car
from service import Service
from order import Order


class AutoRepairShop:
    """Класс Автомастерская"""

    def __init__(self, name):
        self.name = name
        self.clients = []
        self.cars = []
        self.services = []
        self.orders = []
        self.next_order_id = 1

    def add_client(self, full_name, phone):
        """Добавить клиента"""
        client = Client(full_name, phone)
        self.clients.append(client)
        return client

    def add_car(self, brand, model, year, license_plate, owner):
        """Добавить автомобиль"""
        car = Car(brand, model, year, license_plate, owner)
        self.cars.append(car)
        return car

    def add_service(self, name, price):
        """Добавить услугу"""
        service = Service(name, price)
        self.services.append(service)
        return service

    def create_order(self, car, service, date):
        """Создать заказ на ремонт"""
        order = Order(self.next_order_id, car, service, date)
        self.orders.append(order)
        self.next_order_id += 1
        return order

    def list_orders(self):
        """Показать все заказы"""
        if not self.orders:
            print("\n⚠️ Нет активных заказов")
            return

        print(f"\n{'=' * 60}")
        print(f"Заказы автомастерской «{self.name}»")
        print(f"{'=' * 60}")
        for order in self.orders:
            print(order)
            print("-" * 60)


# === ДЕМОНСТРАЦИЯ РАБОТЫ ===
if __name__ == "__main__":
    # Создаём автомастерскую
    shop = AutoRepairShop("Авто-Сервис КубГТУ")

    # Добавляем клиентов
    print("Добавляем клиентов...")
    client1 = shop.add_client("Иванов Иван Иванович", "+7 (918) 123-45-67")
    client2 = shop.add_client("Петрова Мария Сергеевна", "+7 (918) 987-65-43")
    print(f"✅ {client1}")
    print(f"✅ {client2}")

    # Добавляем автомобили
    print("\nДобавляем автомобили...")
    car1 = shop.add_car("ВАЗ", "2114", 2010, "А123ВС 23", client1)
    car2 = shop.add_car("Toyota", "Corolla", 2018, "Е456КМ 23", client2)
    print(f"✅ {car1}")
    print(f"✅ {car2}")

    # Добавляем услуги
    print("\nДобавляем услуги...")
    service1 = shop.add_service("Замена масла и фильтров", 1500)
    service2 = shop.add_service("Диагностика двигателя", 2000)
    print(f"✅ {service1}")
    print(f"✅ {service2}")

    # Создаём заказы
    print("\nСоздаём заказы на ремонт...")
    order1 = shop.create_order(car1, service1, "15.02.2026")
    order2 = shop.create_order(car2, service2, "16.02.2026")
    print(f"✅ {order1}")
    print(f"\n✅ {order2}")

    # Меняем статус первого заказа
    order1.set_status("Готов")
    print(f"\n🔧 Статус заказа №{order1.order_id} изменён на «{order1.status}»")

    # Выводим все заказы
    shop.list_orders()

    print(f"\n{'=' * 60}")
    print("Система автомастерской успешно завершила работу")
    print(f"{'=' * 60}")