from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-balances', methods=['POST'])
def check_balances():
    data = request.json
    api_keys = data.get('api_keys', [])
    
    results = []
    for key in api_keys:
        key = key.strip()
        if not key:
            continue
            
        try:
            response = requests.post(
                "https://api.2captcha.com/getBalance",
                json={"clientKey": key},
                timeout=10
            )
            res_data = response.json()
            if res_data.get('errorId') == 0:
                results.append({
                    "key": f"{key[:4]}...{key[-4:]}",
                    "balance": res_data.get('balance'),
                    "status": "success"
                })
            else:
                results.append({
                    "key": f"{key[:4]}...{key[-4:]}",
                    "error": res_data.get('errorCode', 'Unknown Error'),
                    "status": "error"
                })
        except Exception as e:
            results.append({
                "key": f"{key[:4]}...{key[-4:]}",
                "error": str(e),
                "status": "error"
            })
            
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
