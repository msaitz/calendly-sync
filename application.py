from klein import run, route
from src import calendly
from src.gsheet import event_handler, authenticate, open_sheet


@route('/', methods=['POST'])
def do_post(request):
    content = request.content.read().decode('utf8')
    event = calendly.CalendlyEvent()
    event.add_event(content)

    client = authenticate()
    sheet = open_sheet(client, 'py test')

    event_handler(sheet, event)


run("localhost", 80)
