from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world!'
@app.route('/love')
def love():
    return 'iloveyousummer'
if __name__ =='__main__':
    app.run(debug=False,host='127.0.0.1',port='8080')