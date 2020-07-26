from flask import Flask, jsonify, request 
from Main import *
# creating a Flask app 
app = Flask(__name__) 

# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
	if(request.method == 'GET'): 
		data = "bubu"
		return jsonify({'data': data}) 

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/predict') 
def api_predict():
	if 'API_KEY' in request.args:
		key = request.args['API_KEY']
		if key != 'SRdgcdwzwjIImkskw257MP':
			return 'Invalid API Credentials'
	else:
		return 'Invalid API Credentials'

	if 'ticker' in request.args:
		return call_prediction(request.args['ticker'])
	else:
		return 'Please read API Docs'
	#
	#

def call_prediction(ticker):
	json = prediction(ticker)
	#print(ticker)
	#print(json)
	return jsonify({'data': json}) 

# driver function 
if __name__ == '__main__': 

	app.run(debug = True) 

