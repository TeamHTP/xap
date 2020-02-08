from flask import Flask, request, jsonify
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/authorize', methods= ['GET','POST'])
def authorize():
    # content = request.json

    response = 'decline'
    user = f'{os.environ['SK_KEY']}:'
    command = f'curl https://api.stripe.com/v1/issuing/authorizations/iauth_1CmMk2IyNTgGDVfzFKlCm0gU/{response} -u {user}'
    os.system(command)
    

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=os.environ['PORT'])
 