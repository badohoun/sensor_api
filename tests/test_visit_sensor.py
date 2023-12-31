from sensor_api.fake_data_app.app import VisitSensor
import unittest
from datetime import date


class TestVisitSensor(unittest.TestCase):
    def test_monday_open(self):
        visit_sensor = VisitSensor(1200,300)
        visit_count = visit_sensor.simulate_visit_count(date(2023,9,11))

        self.assertFalse(visit_count==-1)



    def test_tuesday_open(self):
        visit_sensor = VisitSensor(1200,300)
        visit_count = visit_sensor.simulate_visit_count(date(2023,9,12))

        self.assertFalse(visit_count == -1)


    def test_wednesday_open(self):
        visit_sensor = VisitSensor(1200,300)
        visit_count = visit_sensor.simulate_visit_count(date(2023, 9, 13))

        self.assertFalse(visit_count == -1)





    def test_thursday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count =  visit_sensor.simulate_visit_count(date(2023, 9, 14))

        self.assertFalse(visit_count == -1)




    def test_friday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2023, 9, 15))

        self.assertFalse(visit_count == -1)


    def test_saturday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2023, 9, 16))

        self.assertFalse(visit_count == -1)

    def test_sunday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2023, 9, 17))

        self.assertFalse(visit_count == -1)

    def test_with_break(self):
        visit_sensor = VisitSensor(1200, 300,10)
        visit_count = visit_sensor.get_visit_count(date(2023, 11, 22))
        self.assertEqual(visit_count,0)



    def test_with_malfunction(self):
        visit_sensor = VisitSensor(1200,300,0)
        visit_count = visit_sensor.get_visit_count(date(2023,11,28))
        self.assertEqual(visit_count,238)


