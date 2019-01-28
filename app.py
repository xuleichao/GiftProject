from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    template = render_template('sign_in.html')
    return template


if __name__ == '__main__':
    app.run()
