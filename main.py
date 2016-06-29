from flask import Flask,render_template, request
import jinja2
import settings
import octoprintAPI
import json

app = Flask(__name__)
app.debug= True
app.secret_key = 'secret key'

template_dir = 'templates'
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/items/')
def items():
    return render_template('index.jinja2',items = settings.items)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
