import json
import requests

class iot2tangle:
    def __init__(self, j):
        self.data_json = j

    def send_HTTP(self):
        url = "http://192.168.1.115:8080/sensor_data"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        try:
            r = requests.post(url, data=json.dumps(self.data_json), headers=headers)
            print("\t\t   Published in Channel: '" + r.text + "'\n")
        except:
            print("\t\t   --- HTTP Connection Error ---\n")

    def send_MQTT(self):
        print(self.data_json)
