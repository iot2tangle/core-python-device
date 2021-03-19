import json
import requests

# IOT2TANGLE SENDER
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

# IOT2TANGLE BUNDLES
class Bundle:
    global elements
    elements = {}   # Dictionary {"ble-mac": "i2t-json"}

    # Init in 0 (error) 'elements' dict
    def __init__(self, macs):
        for mac in macs:
            elements[mac] = r'{"iot2tangle":[{"sensor":"Error","data":[{"Error":"0"}]}],"device":"' + mac + r'","timestamp":0}'

    # Update the json 
    def update(self, mac, e_json):
        elements[mac] = e_json

    # Concatenation of all the json elements, return an Json I2T bundle string
    def get_json(self):
        json = r'{"bundle":['
        for mac in elements:
            json += elements[mac] + ","
        json = json[:-1]
        json += r']}'
        return json