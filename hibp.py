import requests
from time import sleep


class Hibp:
    def __init__(self, api):
        self.api = api
        self.url = "https://haveibeenpwned.com/api/v3/breachedaccount/{0}"
        self.payload = {}
        self.file = open('mails.txt', 'r')

    def run(self):
        for line in self.file:
            if line.endswith('\n'):
                line = line[:-1]
            try:
                headers = {
                    'hibp-api-key': str(self.api),
                    'format': 'application/json',
                    'timeout': '2.5',
                    'HIBP': str(self.api),
                }
                url = self.url.format(line)
                response = requests.request("GET", url, headers=headers, data=self.payload)
                if response.status_code == 200:
                    print(line)
                    print(response.text)
                    sleep(10)
                else:
                    print(line)
                    print(response.status_code)
                    sleep(10)

            except Exception as e:
                print(e)


constructor = Hibp('aca va la api')       # necesita api y un archivo mails.txt con la lista de mails 1 por linea en el
constructor.run()                         # mismo directorio

# https://stackoverflow.com/questions/64293747/api-integration-with-hibp
