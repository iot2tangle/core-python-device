import json
import requests

class Sender:
    def __init__(self, j):
        if type(j) is type({}):
            j=json.dumps(j)
        self.data_json = j		# Json can be String or Dictionary

    def send_HTTP(self, url):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        try:
            r = requests.post(url, self.data_json, headers=headers)
            print("\t\t   Published in Channel: '" + r.text + "'\n")
        except:
            print("\t\t   --- HTTP Connection Error ---\n")

    def send_MQTT(self):
        print(self.data_json)
