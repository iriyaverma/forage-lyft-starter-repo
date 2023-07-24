from abc import ABC, abstractmethod
from datetime import date

class Car(ABC):
    def __init__(self, last_service_date: date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass

    def engine_should_be_serviced(self) -> bool:
        return self.needs_service()
