import requests
import json
from time import sleep


class Breach:
    def __init__(self, api):
        self.url = "https://breachdirectory.p.rapidapi.com/"
        self.headers = {
                    'X-RapidAPI-Key': api,
                    'X-RapidAPI-Host': 'breachdirectory.p.rapidapi.com'
                }
        self.file = open('mails.txt', 'r')

    def run(self):
        for line in self.file:
            if line.endswith('\n'):
                line = line[:-1]
            try:
                params = {'func': 'auto', 'term': line}
                response = requests.request("GET", self.url, headers=self.headers, params=params)
                print(response.status_code)
                if response.status_code == 200:
                    print(line)
                    data = response.json()
                    print(data)
                    sleep(3)
                else:
                    print(line)
                    print(response.status_code)
                    sleep(3)

            except Exception as e:
                print(e)


constructor = Breach('put your api here') # necesita api y un archivo mails.txt con la lista de mails 1 por linea en el
constructor.run()                         # mismo directorio
