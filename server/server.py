from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
from game_state import GameState

# Connecting my MySQL database
import mysql.connector
# Get the environment variables for the credentials
from dotenv import load_dotenv
import os

load_dotenv()
def startDatabase():
    database = mysql.connector.connect(
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME"),
        host = os.getenv("DB_HOST")
    )
    return database

def updateIntDb(value):
    database = startDatabase()
    # Create a cursor from the connection
    cursor = database.cursor()
    # Define the SQL UPDATE statement.
    # Execute the query with the provided parameters
    cursor.execute("UPDATE game_deck_table SET value = %s WHERE id = 0", (value,))
    # Commit the changes
    database.commit()
    # Close the cursor and connection
    cursor.close()
    database.close()


# Get INT from the database
def getIntDb():
    database = startDatabase()
    # Create a cursor object
    cursor = database.cursor()
    # Execute the SELECT query to fetch the value
    cursor.execute("SELECT value FROM game_deck_table WHERE id = 0")
    # Fetch the result
    result = cursor.fetchone()
    # Check if there is a result and print it
    if result == False:
        print("No data found.")
    # Close the cursor and connection
    cursor.close()
    database.close()
    return result[0]

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes by passing the Flask app instance to CORS

# POST Request to send symbol and train on the data
@app.route('/checkConnection', methods=['POST'])
def checkConnection():
    print("Server : Request Received Connection Succesful!")
    message = "Client : Response Received Connection Succesful!"
    return jsonify(message)

# POST Request to send symbol and train on the data
@app.route('/createGame', methods=['POST'])
def createGame():

    # Grab the current value and increment it
    updateIntDb( int(getIntDb()) + 1)

    print("Server : Created Game Session!")
    message = "Client : Created Game Session!"
    return jsonify(message)

# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

'''
    cd to my-app, command below to run the project
    npm run dev

'''