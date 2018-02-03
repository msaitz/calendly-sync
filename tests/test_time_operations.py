from src import time_operations
import unittest
import datetime


class TestTimeOperations(unittest.TestCase):
    def setUp(self):
        self.slots = time_operations.get_timeslots()

    def test_timeSlot(self):
        self.assertEqual(len(self.slots), 24)
        self.assertEqual(self.slots['10:00'], 0)
        self.assertEqual(self.slots['15:45'], 23)

    def test_monday(self):
        self.day = datetime.datetime(2018, 1, 5)
        self.next_monday = datetime.datetime(2018, 1, 8)
        self.this_monday = datetime.datetime(2018, 1, 1)
        self.assertEqual(time_operations.get_next_monday(self.day), self.next_monday)
        self.assertEqual(time_operations.get_this_monday(self.day), self.this_monday)

