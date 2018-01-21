import requests
import json


class Calendly(object):
    _api_key = {'X-TOKEN': 'LIMHDEAGLGPFC4XOFLYO23CPYNKOMNBD'}
    _name = ''
    _time = ''
    _index = None
    _type = None

    def echo(self):
        r = requests.get('https://calendly.com/api/v1/echo', headers=self._api_key)
        if json.loads(r.text)['email']:
            return True
        else:
            return False

    def get_key(self):
        print(self._api_key)
        return self._api_key

    def get_subscriptions(self):
        if self.echo():
            r = requests.get('https://calendly.com/api/v1/hooks', headers=self._api_key)
            content = json.loads(r.text)
            if content['data']:
                return content['data']
        else:
            return ''








