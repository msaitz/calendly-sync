from os import path


def load_file(filename):
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, 'static/' + filename))
    with open(filepath) as file:
        return file.read()


def json_path(filename):
    basepath = path.dirname(__file__)
    return path.abspath(path.join(basepath, 'static/' + filename))


