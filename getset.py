class BatterySystem:
    def __init__(self, battery=100):
        self.__battery = 100
        self.battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        if value < 0:
            self.__battery = 0
        elif value > 100:
            self.__battery = 100
        else:
            self.__battery = value

    def info(self):
        print(f"Батарея деңгейі: {self.battery}%")


class StorageSystem:
    def __init__(self, total_storage=128):
        self.__total_storage = total_storage
        self.__used_storage = 0

    @property
    def total_storage(self):
        return self.__total_storage

    @property
    def used_storage(self):
        return self.__used_storage

    @used_storage.setter
    def used_storage(self, value):
        if value < 0:
            self.__used_storage = 0
        elif value > self.__total_storage:
            self.__used_storage = self.__total_storage
        else:
            self.__used_storage = value

    def install(self, size):
        if self.used_storage + size > self.total_storage:
            print("Жад жеткіліксіз! Орнату мүмкін емес.")
        else:
            self.used_storage += size
            print(f"{size}GB орнатылды.")

    def delete(self, size):
        if size > self.used_storage:
            print("Мұнша көлемді өшіру мүмкін емес.")
        else:
            self.used_storage -= size
            print(f"{size}GB өшірілді.")

    def info(self):
        free = self.total_storage - self.used_storage
        print(f"Жад: {self.used_storage}GB қолданылды, {free}GB бос (барлығы {self.total_storage}GB)")


class Smartphone:
    def __init__(self, model, battery=100, storage=128):
        self.model = model
        self.battery_system = BatterySystem(battery)
        self.storage_system = StorageSystem(storage)

    def install_app(self, size):
        self.storage_system.install(size)
        self.battery_system.battery -= 5

    def delete_app(self, size):
        self.storage_system.delete(size)

    def charge(self, percent):
        self.battery_system.battery += percent
        print(f"Телефон зарядталды. Қазір: {self.battery_system.battery}%")

    def info(self):
        print("\nТелефон ақпараты")
        print(f"Модель: {self.model}")
        self.battery_system.info()
        self.storage_system.info()

model = input("Телефон моделін енгізіңіз: ")
battery = int(input("Батарея деңгейін енгізіңіз: "))
storage = int(input("Жалпы жад көлемін енгізіңіз: "))

phone = Smartphone(model, battery, storage)

phone.info()

size_install = int(input("\nОрнатылатын қосымшаның көлемі (GB): "))
phone.install_app(size_install)

size_delete = int(input("Өшірілетін қосымшаның көлемі (GB): "))
phone.delete_app(size_delete)

charge_percent = int(input("Қанша пайыз зарядтайсыз?: "))
phone.charge(charge_percent)

print("\nСоңғы телефон ақпараты:")
phone.info()
