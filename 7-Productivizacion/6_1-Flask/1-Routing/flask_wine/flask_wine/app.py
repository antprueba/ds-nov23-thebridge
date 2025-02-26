from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import os


app = Flask(__name__)

@app.route('/health/', methods=['GET'])
def health():
    return "everything is here"

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)

#os.path.dirname(os.path.realpath(__file__)) + './models/final_prediction.pickle'
modelfile = './6_1-Flask/1-Routing/flask_wine/flask_wine/models/final_prediction.pickle'
model = p.load(open(modelfile, 'rb'))

print(type(model))

if __name__ == "__main__":
    print("hello")
    app.run(debug=False)