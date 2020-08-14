from flask import Flask, Response
from subprocess import call
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(filename='error.log',level=logging.DEBUG)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/water')
def water_plants():
    call(["python", "../pump.py"])
    return Response('watering the lovely plants')

if __name__ == "__main__":
        app.run(host="0.0.0.0",debug=True)
