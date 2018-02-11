from src.time_operations import *
from datetime import datetime
import unittest

class TestTimeOperations(unittest.TestCase):

    def test_timeSlot(self):
        self.slots = get_timeslots()
        self.assertEqual(len(self.slots), 24)
        self.assertEqual(self.slots['10:00'], 0)
        self.assertEqual(self.slots['15:45'], 23)

    def test_next_monday(self):
        self.day = datetime(2018, 1, 5)
        self.next_monday = datetime(2018, 1, 8)
        self.assertEqual(next_monday(self.day), self.next_monday)

    # test will fail after 2018!
    def test_full_week(self):
        self.monday = datetime(2018, 1, 8)
        self.friday = datetime(2018, 1, 12)
        weekdays = full_week(self.monday)
        self.assertEqual(weekdays[0], self.monday)
        self.assertEqual(weekdays[4], self.friday)

    # test will fail after 2018!
    def test_first_monday_month(self):
        self.assertEqual(first_monday_month(1).day, 1)
        self.assertEqual(first_monday_month(5).day, 7)
        self.assertEqual(first_monday_month(8).day, 6)
        self.assertEqual(first_monday_month(12).day, 3)

    # test will fail too after 2018!
    def test_number_mondays_month(self):
        self.assertEqual(number_mondays_month(1), 5)
        self.assertEqual(number_mondays_month(2), 4)
        self.assertEqual(number_mondays_month(4), 5)
        self.assertEqual(number_mondays_month(12), 5)
