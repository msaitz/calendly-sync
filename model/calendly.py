import requests
import datetime

from model import timeslots


class CalendlyEvent:
    def __init__(self):
        self.api_key = {'X-TOKEN': 'LIMHDEAGLGPFC4XOFLYO23CPYNKOMNBD'}
        self._name = None
        self._date = None
        self._time_index = None
        self._event_type = None

    @property
    def name(self): return self._name

    @property
    def time(self): return self._date.strftime('%H:%M')

    @property
    def day(self): return self._date.strftime('%d')

    @property
    def month(self): return self._date.strftime('%m')

    @property
    def year(self): return self._date.strftime('%y')

    @property
    def time_index(self): return self._time_index

    @property
    def event_type(self): return self._event_type

    def echo(self):
        r = requests.get('https://calendly.com/api/v1/echo', headers=self.api_key)
        content = eval(r.text)
        if content['email']:
            return True
        else:
            return False

    def get_subscriptions(self):
        if self.echo():
            r = requests.get('https://calendly.com/api/v1/hooks', headers=self.api_key)
            content = eval(r.text)
            if content['data']:
                return content['data']
        else:
            return None

    def add_event(self, data):
        formatted_data = self._parse_raw_data(data)

        if formatted_data['event'] == 'invitee.created':
            formatted_data = formatted_data['payload']
            self._name = formatted_data['invitee']['name']
            self._date = self._parse_date(formatted_data)
            self._time_index = self._get_time_index(self._date.strftime('%H:%M'))
            self._event_type = formatted_data['event_type']['slug']
            return True
        else:
            return False

    @staticmethod
    def _parse_raw_data(data):
        data = data.replace('null', 'None')
        data = data.replace('true', 'True')
        data = data.replace('false', 'False')
        data = eval(data)
        return data

    @staticmethod
    def _get_time_index(time):
        slots = timeslots.TimeSlots()
        return slots.timeslots[time]

    # slice string, current format is '03:30pm - Friday, January 26, 2018'
    @staticmethod
    def _parse_date(data):
        event_time = data['event']['start_time_pretty']
        return datetime.datetime.strptime(event_time, '%I:%M%p - %A, %B %d, %Y')












