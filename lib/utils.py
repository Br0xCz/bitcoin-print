import yaml
import json
import os

def loadFromFile(file_name):
    fileContents = ''
    path = '/'.join(os.path.dirname(__file__).split('/')[0:-1])
    with open((os.path.join(path,file_name)), 'r') as file:
        fileContents = file.read()
        file.close()
    return fileContents

def loadConfig(file_name):
    return yaml.load(loadFromFile(file_name))

def loadJsonObject(file_name):
    return json.loads(loadFromFile(file_name))

def removeUnnecessaryData(config):
    for printer in config['printers']:
        config['printers'][printer] = {
            'name': config['printers'][printer]['name'],
            'url': config['printers'][printer]['url'],
        }
    return config


def translatePrinterNamesToPrinterObjects(printerNames, printersConfig):
    printers = {}
    for printerName in printerNames:
        printers[printerName] = printersConfig['printers'][printerName]
    return printers