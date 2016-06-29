from flask import Flask,render_template
import jinja2
import settings
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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
