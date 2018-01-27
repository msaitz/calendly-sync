from datetime import datetime, timedelta


class TimeSlots:
    def __init__(self):
        self._timeslots = self._get_timeslots(24)

    @property
    def timeslots(self): return self._timeslots

    def _get_timeslots(self, n):
        start = datetime.strptime('10:00', '%H:%M')
        return {self._add_time(start, i).strftime('%H:%M'): i for i in range(n)}

    @staticmethod
    def _add_time(time, n):
        return time + timedelta(minutes=15 * n)





