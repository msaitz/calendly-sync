from os import path


def load_file(filename):
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, 'static/' + filename))
    with open(filepath) as file:
        api_key = file.readline()
    return api_key
