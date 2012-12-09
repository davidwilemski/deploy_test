
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! This page is an exercise in automated deployment <a href="https://github.com/davidwilemski/deploy_test">https://github.com/davidwilemski/deploy_test</a>.'

if __name__ == '__main__':
    app.run(debug=True)
