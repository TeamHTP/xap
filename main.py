from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/authorize', methods= ['GET','POST'])
def authorize():
    # content = request.json
    return 'Hey'
   
    # print(content)
    # return False
    

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='localhost', debug=True)


 