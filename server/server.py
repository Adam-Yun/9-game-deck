from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes by passing the Flask app instance to CORS

# POST Request to send symbol and train on the data
@app.route('/checkConnection', methods=['POST'])
def checkConnection():
    print("Server : Request Received Connection Succesful!")
    message = "Client : Response Received Connection Succesful!"
    return jsonify(message)

# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)