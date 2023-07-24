from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class CarEngine:
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self, threshold_years: int) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + threshold_years)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()
