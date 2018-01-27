from klein import run, route
from model import calendly


@route('/', methods=['POST'])
def do_post(request):
    event = calendly.CalendlyEvent()
    event.add_event(request)

    print(event.name + ' ' + event.time + ' ' + event.day + ' ' + event.month)
    print(event.event_type)


run("localhost", 8080)
