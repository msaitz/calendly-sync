from os import path
from oauth2client.service_account import ServiceAccountCredentials


def load_file(filename):
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, 'static/' + filename))
    with open(filepath) as file:
        return file.read()


def json_path(filename):
    basepath = path.dirname(__file__)
    return path.abspath(path.join(basepath, 'static/' + filename))


