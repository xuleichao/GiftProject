from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/egg')
def hello_world():
    template = render_template('sign_in.html')
    return template


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
