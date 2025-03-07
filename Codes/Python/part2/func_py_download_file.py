# func_py_download_file.py
import requests

def func_py_download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    return f"Saved {filename}"

print(func_py_download_file("https://example.com/file.zip", "download.zip"))
