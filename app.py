from flask import Flask
from blueprints.placeholder import placeholder

app = Flask(__name__)
app.register_blueprint(placeholder, url_prefix="/placeholder")


@app.route('/')
def index():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
