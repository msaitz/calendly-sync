from src import time_operations
from src.parse_operations import parse_date, parse_raw_data
import requests
import helpers


class CalendlyEvent:
    def __init__(self):
        self.api_key = {'X-TOKEN': helpers.load_file('apikey.txt')}
        self._name = None
        self._date = None
        self._time_index = None
        self._event_type = None
        self._canceled = False

    @property
    def date(self): return self._date

    @property
    def name(self): return self._name

    @property
    def is_canceled(self): return self._canceled

    @property
    def formatted_date(self): return self._date.strftime('%d/%m/%y')

    @property
    def time(self): return self._date.strftime('%H:%M')

    @property
    def day(self): return self._date.strftime('%d')

    @property
    def month(self): return int(self._date.strftime('%m'))

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
        formatted_data = parse_raw_data(data)

        if formatted_data['event']:
            formatted_data = formatted_data['payload']

            if formatted_data['invitee']['canceled']:
                self._date = parse_date(formatted_data)
                self._canceled = True
            else:
                self._date = parse_date(formatted_data)
                self._name = formatted_data['invitee']['name']
                self._event_type = self.select_event_type(formatted_data)

            self._time_index = time_operations.time_index(self._date.strftime('%H:%M'))

            return True
        else:
            return False

    @staticmethod
    def select_event_type(data):
        options = {'15min': 'Surgery',
                   'mobilehandover': 'Phone',
                   'ict-ipad-tablet-handover': 'iPad'}

        return options[data['event_type']['slug']]

    # for testing purposes
    def change_date(self, new_date):
        self._date = new_date









