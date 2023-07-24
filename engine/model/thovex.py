from datetime import datetime

class Thovex(CapuletEngine):
    def needs_service(self) -> bool:
        return CarEngine.needs_service(self, threshold_years=4)
