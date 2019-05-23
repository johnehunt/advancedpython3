from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def welcome():
    return jsonify({'msg': 'Hello Flask World'})


app.run(debug=True)

