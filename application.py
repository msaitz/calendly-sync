from klein import run, route
from model import calendly


@route('/', methods=['POST'])
def do_post(request):
    content = request.content.read().decode('utf8')
    event = calendly.CalendlyEvent()
    event.add_event(content)

    print(event.name + ' ' + event.time + ' ' + event.day + ' ' + event.month)
    print(event.event_type)


run("localhost", 80)
