class TemperatureSystem:
    def __init__(self, temperature = 22):
        self.__temperature = 22
        self.temperature = temperature

    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, value):
        self.__temperature = value

        if self.__temperature < 10:
            print("Ескерту!!! Температура тым төмен!")
        elif self.__temperature > 35:
            print("Ескерту!!! Температура тым жоғары!")

class SecuritySystem:
    def __init__(self, status = True):
        self.__status = True
        self.status = status

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, value):
        self.__status = value
        if not self.__status:
            print("Ескерту!!! Қауіпсіздік бұзылды! Үйге біреу кірген болуы мүмкін!")


class SmartHome:
    def __init__(self, home_name, temperature = 22, security_status = True):
        self.home_name = home_name
        self.temp_system = TemperatureSystem(temperature)
        self.security_system = SecuritySystem(security_status)

    def info(self):
        print(f"Үй атауы: {self.home_name}")
        print(f"Температура: {self.temp_system.temperature}С")

        if self.security_system.status == True:
            print("Қауіпсіздік: Қалыпты")
        else:
            print("Қауіпсіздік: Қауіпті")


home_name = input("Үй атауын енгіз: ")
temperature = int(input("Температураны енгіз: "))
security = input("Қауіпсіздік қосулы ма? (Ия/Жоқ): ")
security_status = True if security == "Ия" else False

home = SmartHome(home_name, temperature, security_status)
home.info()





