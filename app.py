from flask import Flask,jsonify,request
import requests

key=""
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
    
if __name__ == '__main__':
    app.run(debug=True)