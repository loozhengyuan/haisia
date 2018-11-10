from flask import Blueprint

app = Blueprint('haisia', __name__)

@app.route('/', methods=['POST'])
def index():
    req = request.json
    res = handler(req)
    return jsonify(res)

def handler(req):
    intent = req['queryResult']['intent']['displayName']
    params = req['queryResult']['parameters']

    if intent in ['basic-info-intent']:
        brand = params['brand']
        fulfillment = data.basic_info_intent[brand]
    elif intent in ['distrib-info-intent']:
        distrib = params['distrib']
        fulfillment = data.distrib_info_intent[distrib]
    elif intent in ['fish-info-intent']:
        fish = params['fish']
        fulfillment = data.fish_info_intent[fish]
    elif intent in ['recipes-intent']:
        fish = params['fish']
        fulfillment = data.recipes_intent[fish]

    res_raw = {
        "fulfillmentMessages": fulfillment
        }
    
    return res_raw