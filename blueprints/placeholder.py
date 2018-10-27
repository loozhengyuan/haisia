from flask import Blueprint

placeholder = Blueprint('placeholder', __name__)


@placeholder.route('/')
def index():
    return "Hello World!"
