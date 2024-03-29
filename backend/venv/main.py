from flask import Flask,jsonify
from flask_cors import CORS


app=Flask(__name__)

app.config.from_object(__name__)

CORS(app,resources={r"/*":{'origins':'*'}})

CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})



@app.route('/',methods=['GET'])
def home():
    return("Hello World")

if __name__ == '__main__':
    app.run(debug=True) 