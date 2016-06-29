import requests
import json

def startPrint(fileName, apiKey, address):
    url = 'http://' + address + '/api/files/local/' + fileName
    headers = {'X-Api-Key': apiKey}
    command = {
        'command': 'select',
        'print': True,
    }
    r = requests.post(url, json=command, headers=headers)
    return r, json.loads(r.text)
