import json


def convert_to_jason(string):
    #if string[0] is "'":
    #    formatted_str = string.replace("'", "\"")
    return json.load(string)
    #else:
    #    return ''
