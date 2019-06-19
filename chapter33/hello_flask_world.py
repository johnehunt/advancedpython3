from flask import Flask, jsonify

# Initialise Flask
app = Flask(__name__)


# Create a mapping from URL to function
@app.route('/hello', methods=['GET'])
def welcome():
    return jsonify({'msg': 'Hello Flask World'})


# Start up the web service
app.run(debug=True)
