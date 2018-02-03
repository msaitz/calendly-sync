import datetime

TIMESLOTS = 24


def get_timeslots():
    start = datetime.datetime.strptime('10:00', '%H:%M')
    return {add_time(start, i).strftime('%H:%M'): i for i in range(TIMESLOTS)}


def add_time(time, index):
    return time + datetime.timedelta(minutes=15 * index)


def get_time_index(time):
    slots = get_timeslots()
    return slots[time]


def get_next_monday(day):
    monday = 0
    days_ahead = monday - day.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return day + datetime.timedelta(days_ahead)


def get_this_monday(day):
    days_ahead = day.weekday() * -1
    return day + datetime.timedelta(days_ahead)


def get_full_week(day):
    monday = get_next_monday(day)
    return [monday + datetime.timedelta(i) for i in range(0, 4)]





