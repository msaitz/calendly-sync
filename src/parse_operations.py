from datetime import datetime


def parse_raw_data(data):
    data = data.replace('null', 'None')
    data = data.replace('true', 'True')
    data = data.replace('false', 'False')
    data = eval(data)

    return data


# slice string, current format is '03:30pm - Friday, January 26, 2018'
def parse_date(data):
    '''
    if webhook_type == 'create':
        event_time = data['event']['start_time']
    else:
    '''
    event_time = data['event']['start_time']
    return datetime.strptime(event_time, '%Y-%m-%dT%H:%M:%S+00:00')
