# func_py_read_json_file.py
import json

def func_py_read_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

print(func_py_read_json_file("data.json"))
