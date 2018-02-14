from datetime import datetime, timedelta

TIMESLOTS = 24


# generates the timeslots for containing the booking strings.
def get_timeslots():
    start = datetime.strptime('10:00', '%H:%M')
    return {add_time(start, i).strftime('%H:%M'): i for i in range(TIMESLOTS)}


# helper function for get_timeslots.
def add_time(time, index):
    return time + timedelta(minutes=15 * index)


def time_index(time):
    slots = get_timeslots()
    return slots[time]


# returns a list of datetime objects of 5 consecutive days starting from a monday
def full_week(day):
    if day.weekday() != 0:
        return []
    return [day + timedelta(i) for i in range(0, 5)]


# returns a datetime object with the next Monday of a given date
def next_monday(day):
    days_ahead = (day.weekday() * -1) + 7
    return day + timedelta(days=days_ahead)


# returns the number of the month of the first day that is monday
def first_monday_month(month):
    year = datetime.now().year
    start = datetime(year, month, 1)

    if month + 1 >= 12:
        month = 1

    end = datetime(year, month + 1, 1) - timedelta(days=1)
    current = start
    while start.day < end.day:
        if current.weekday() == 0:
            return current
        current += timedelta(days=1)

    return -1


# returns the number of mondays occurrences of a month
def number_mondays_month(month):
    year = datetime.now().year
    iterator = datetime(year, month, first_monday_month(month).day)

    count = 0
    while iterator.month == month:
        if iterator.weekday() == 0:
            count += 1
        iterator += timedelta(days=7)

    return count


def get_month_for_date(date):
    month = date.month
    if date < first_monday_month(date.month):
        month = date.month - 1
    return month


def first_day_week(date):
    monday = date - timedelta(days=date.weekday())
    return monday
