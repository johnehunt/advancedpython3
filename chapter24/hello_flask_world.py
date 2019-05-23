from flask import Flask, jsonify, url_for


app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def welcome():
    return jsonify({'msg': 'Hello Flask World'})

with app.test_request_context():
    print(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)
