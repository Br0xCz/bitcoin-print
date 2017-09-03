from flask import Flask,render_template, request
import jinja2
import settings
import octoprintAPI
from lib.utils import loadConfig, translatePrinterNamesToPrinterObjects, removeUnnecessaryData
from lib.requests import makeRequest
import json

app = Flask(__name__)
app.debug= True
app.secret_key = 'secret key'

template_dir = 'templates'
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

COMMAND_PRINT = 'COMMAND_PRINT'
COMMAND_PAUSE = 'COMMAND_PAUSE'
COMMAND_RESUME = 'COMMAND_RESUME'
COMMAND_LOAD = 'COMMAND_LOAD'
COMMAND_CANCEL = 'COMMAND_CANCEL'
COMMAND_LOAD_FILE = 'COMMAND_LOAD_FILE'
COMMAND_PREHEAT= 'COMMAND_PREHEAT'

PRINTERS_CONFIG_PATH = './printers.yml'

def getSelectedPrinters():
    return request.form['selectedPrinters'].split(',')

@app.route('/')
def index():
    return render_template('index.jinja2',items = settings.items)

@app.route('/api/printer-config')
def printerConfig():
    return json.dumps(removeUnnecessaryData(loadConfig('./printers.yml')))

@app.route('/api/ready')
def printerState():
    r,data = octoprintAPI.getInfo(settings.settings['printer']['address'],settings.settings['printer']['api-key'])
    ready = False
    if(data['state']['flags']['ready'] and data['state']['flags']['printing']):
        ready = True
    response = {
        'ready': ready
    }
    return json.dumps(response)

@app.route('/api/load/<string:fileName>', methods=['POST'])
def loadFile(fileName):
    response = makeRequest(COMMAND_LOAD_FILE,
                translatePrinterNamesToPrinterObjects(getSelectedPrinters(), loadConfig(PRINTERS_CONFIG_PATH)),
                fileName)
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
