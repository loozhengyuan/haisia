from flask import Flask, redirect, url_for
from blueprints.placeholder import placeholder

app = Flask(__name__)
app.register_blueprint(placeholder, url_prefix="/placeholder")


@app.route('/')
def index():
    return redirect(url_for('api'))


@app.route('/api')
def api():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
