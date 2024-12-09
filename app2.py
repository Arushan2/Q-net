from flask import Flask,jsonify
import requests

key=""
app = Flask(__name__)
@app.route('/test-repliers-map', methods=['GET'])
def test():
    url = "https://api.repliers.io/listings?cluster=true&clusterFields=mlsNumber,listPrice,address.city&listings=false&clusterPrecision=10"
    headers = {
        "REPLIERS-API-KEY": key,
        "Content-Type": "application/json"
    }
    try:
        response=requests.get(url,headers=headers)
        return jsonify({
            "status": response.status_code,
            "data": response.json()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)