from klein import run, route
import json


@route('/', methods=['POST'])
def do_post(request):
    content = json.loads(request.content.read())
    response = json.dumps(dict(the_data=content))
    print(response)
    return response


run("localhost", 8080)
