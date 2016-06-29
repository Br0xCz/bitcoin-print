import octoprintAPI
import settings

def startPrint(filename):
    octoprintAPI.startPrint(filename,settings.settings['printer']['api-key'],settings.settings['printer']['address'])