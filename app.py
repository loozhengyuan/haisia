from flask import Flask, redirect, url_for
from blueprints import haisia

app = Flask(__name__)
app.register_blueprint(haisia.app, url_prefix="/api/haisia")


@app.route('/')
def index():
    return redirect(url_for('api'))


@app.route('/api')
def api():
    return "Welcome to API Server!"


if __name__ == '__main__':
    app.run()
