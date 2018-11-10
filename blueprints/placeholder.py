from flask import Blueprint

app = Blueprint('placeholder', __name__)

@app.route('/')
def index():
    return "Hello World!"
