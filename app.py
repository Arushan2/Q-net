from flask import Flask,jsonify,request
import requests
from creds import key

app = Flask(__name__)
@app.route('/test-repliers', methods=['GET'])
def test():
    search_query = request.args.get('search', '') 
    url = f"https://api.repliers.io/listings?{search_query}"
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
    
@app.route('/test-repliers-map', methods=['GET'])
def test_map():
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
    
@app.route('/test-repliers-geo', methods=['GET'])
def test_geo_map():
    # Base URL
    url = "https://api.repliers.io/listings"
    
    map_parameter = [
        [
            [-79.3928178512883, 43.65790500294517],
            [-79.40145579410431, 43.651653527879944],
            [-79.38874165704074, 43.64991005052994],
            [-79.3928178512883, 43.65790500294517]
        ]
    ]
    
    params = {
        "cluster": "true",
        "clusterFields": "mlsNumber,listPrice,address.city",
        "listings": "false",
        "clusterPrecision": 10,
        "map": str(map_parameter) 
    }
    
    headers = {
        "REPLIERS-API-KEY": key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        return jsonify({
            "status": response.status_code,
            "data": response.json()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/test-repliers-geo-post', methods=['POST'])
def test_geo_map_post():
    url = "https://api.repliers.io/listings"
    
    data = request.json
    
    # Headers
    headers = {
        "REPLIERS-API-KEY": key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        return jsonify({
            "status": response.status_code,
            "data": response.json()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)