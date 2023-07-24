from datetime import date

class Car:
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

class Calliope(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__(current_date, last_service_date, current_mileage, last_service_mileage)

class Glissade(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__(current_date, last_service_date, current_mileage, last_service_mileage)

class Palindrome(Car):
    def __init__(self, current_date: date, last_service_date: date, warning_light_on: bool):
        super().__init__(current_date, last_service_date, 0, 0)  # 0 mileage since it's not applicable for Palindrome

class Rorschach(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__(current_date, last_service_date, current_mileage, last_service_mileage)

class Thovex(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__(current_date, last_service_date, current_mileage, last_service_mileage)
