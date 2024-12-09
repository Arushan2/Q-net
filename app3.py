from flask import Flask, jsonify, request
import requests

key = ""
app = Flask(__name__)

@app.route('/test-repliers-map-post', methods=['POST'])
def test_post():
    url = "https://api.repliers.io/listings?listings=true&operator=AND&sortBy=updatedOnDesc&status=A"
    headers = {
        "REPLIERS-API-KEY": key,
        "accept": "application/json",
        "content-type": "application/json"
    }
    try:
        # Pass the JSON body from the request to the API
        response = requests.post(url, headers=headers, json=request.json)
        return jsonify({
            "status": response.status_code,
            "data": response.json()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
