from flask import Flask, request, jsonify
import os
import xpring
import requests

app = Flask(__name__)



def get_XPR_to_USD():
    COINLAYER_URL = "http://api.coinlayer.com/api/live"
    COINLAYER_PARAMS = {'access_key': os.environ["COINLAYER_KEY"]}

    r = requests.get(url = COINLAYER_URL, params = COINLAYER_PARAMS)
    exchange_data = r.json()

    return exchange_data['rates']['XRP']


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/authorize', methods= ['GET','POST'])
def authorize():
    content = request.json
    response = 'decline'
    user = f'{os.environ["SK_KEY"]}:'
    auth_id = content['id']
    command = f'curl https://api.stripe.com/v1/issuing/authorizations/{auth_id}/{response} -u {user}'
    os.system(command)


# @app.route('/transfer', methods=['POST'])
# def transfer():
#     content = request.json
#     wallet_seed = content['wallet_seed']
#     amount = content['amount']
#     # host_seed = os.environ['HOST_SEED']
#     wallet = xpring.Wallet.from_seed(wallet_seed)
#     url = 'grpc.xpring.tech:80'
#     client = xpring.Client.from_url(url)

    

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=os.environ['PORT'])
 