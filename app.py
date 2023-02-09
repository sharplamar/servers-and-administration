from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

@app.route('/shuffle', methods=['GET'])
def index():
    data = request.get_json()

    l = list(data.items())
    random.shuffle(l)
    # shuffled_data = json.dumps(l)
    d = dict(l)
    shuffled_data = json.dumps(d)
    
    return shuffled_data


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')