# import Flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# create Flask app
app = Flask(__name__)

dummy_data = [
    {
    'id': 1,
    'substance': 'CO2',
    'amount': '1.5',
    'unit': 'kg',
    'danger_level': 'high',
},
{
    'id': 2,
    'substance': 'CO',
    'amount': '3.5',
    'unit': 'kg',
    'danger_level': 'very high',
}
    ]

def retrieve_data():
    return dummy_data

# create a main route
@app.route('/')
def index():
    return 'Hello, World!'

# create a 'post' route to send data to the server
@app.route('/data/get', methods=['GET'])
def get_data():
    # return the data from retrieve_data()
    return jsonify(retrieve_data())

# create a 'post' route to send data to the server (id specified)
@app.route('/data/get/<item_id>', methods=['GET'])
def get_data_by_id(item_id):
    # return the data from retrieve_data()
    return jsonify(retrieve_data()[int(item_id) - 1])

# run the app
if __name__ == '__main__':
    app.run(debug=True)

