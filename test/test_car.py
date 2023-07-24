import unittest
from datetime import datetime
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestCar(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def test_needs_service_battery(self):
        test_data = [
            (self.today.replace(year=self.today.year - 3), 0, 0, True),
            (self.today.replace(year=self.today.year - 1), 0, 0, False),
            (self.today.replace(year=self.today.year - 5), False, True, True),
            (self.today.replace(year=self.today.year - 3), False, True, False)
        ]

        for last_service_date, current_mileage, last_service_mileage, expected in test_data:
            with self.subTest(last_service_date=last_service_date,
                              current_mileage=current_mileage,
                              last_service_mileage=last_service_mileage,
                              expected=expected):
                car = Calliope(last_service_date, current_mileage, last_service_mileage)
                self.assertEqual(car.needs_service(), expected)

                car = Glissade(last_service_date, current_mileage, last_service_mileage)
                self.assertEqual(car.needs_service(), expected)

    def test_needs_service_engine(self):
        test_data = [
            (self.today, 30001, 0, True),
            (self.today, 30000, 0, False),
            (self.today, 60001, 0, True),
            (self.today, 60000, 0, False),
            (self.today, 30001, 0, True),
            (self.today, 30000, 0, False)
        ]

        for last_service_date, current_mileage, last_service_mileage, expected in test_data:
            with self.subTest(last_service_date=last_service_date,
                              current_mileage=current_mileage,
                              last_service_mileage=last_service_mileage,
                              expected=expected):
                car = Calliope(last_service_date, current_mileage, last_service_mileage)
                self.assertEqual(car.needs_service(), expected)

                car = Glissade(last_service_date, current_mileage, last_service_mileage)
                self.assertEqual(car.needs_service(), expected)

                car = Rorschach(last_service_date, current_mileage, last_service_mileage)
                self.assertEqual(car.needs_service(), expected)

                car = Thovex(last_service_date, current_mileage, last_service_mileage)
                self.assertEqual(car.needs_service(), expected)


if __name__ == '__main__':
    unittest.main()
