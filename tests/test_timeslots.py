import unittest
from model import timeslots


class TestTimeslots(unittest.TestCase):

    def setUp(self):
        self.slots = timeslots.TimeSlots()

    def test_constructor(self):
        self.assertIsNotNone(self.slots)
        self.assertEqual(len(self.slots.timeslots), 24)
        self.assertEqual(self.slots.timeslots['10:00'], 0)
        self.assertEqual(self.slots.timeslots['15:45'], 23)
