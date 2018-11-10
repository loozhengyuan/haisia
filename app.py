from flask import Flask, redirect, url_for
from blueprints import placeholder

app = Flask(__name__)
app.register_blueprint(placeholder.app, url_prefix="/api/placeholder")


@app.route('/')
def index():
    return redirect(url_for('api'))


@app.route('/api')
def api():
    return "Welcome to API Server!"


if __name__ == '__main__':
    app.run()
