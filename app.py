# import header.py
from header import *

# create Flask app
app = Flask(__name__)

dummy_data = [
    {
    'id': 1,
    'substance': 'CO2',
    'amount': '5',
    'unit': 'kg',
    'danger_level': 'high',
    'time_stamp': '2019-01-01'
    },
    {
    'id': 2,
    'substance': 'CO',
    'amount': '10',
    'unit': 'kg',
    'danger_level': 'very high',
    'time_stamp': '2019-01-01'
    },
    {
    'id': 3,
    'substance': 'NO2',
    'amount': '25',
    'unit': 'kg',
    'danger_level': 'high',
    'time_stamp': '2019-01-01'
    },
    {
    'id': 4,
    'substance': 'NO',
    'amount': '50',
    'unit': 'kg',
    'danger_level': 'very high',
    'time_stamp': '2019-01-01'
    },
    {
    'id': 5,
    'substance': 'O3',
    'amount': '100',
    'unit': 'kg',
    'danger_level': 'high',
    'time_stamp': '2019-01-01'
    },
    {
    'id': 6,
    'substance': 'SO2',
    'amount': '14',
    'unit': 'kg',
    'danger_level': 'high',
    'time_stamp': '2019-01-01'
    },

]

def retrieve_data():
    return dummy_data

# create a main route
@app.route('/')
def index():
    return 'Hello, World!'

# create a 'get' route to send data to the server
@app.route('/data/get', methods=['GET'])
def get_data():
    # return the data from retrieve_data()
    return jsonify(retrieve_data())

# create a 'get' route to send data to the server (id specified)
@app.route('/data/get/<item_id>', methods=['GET'])
def get_data_by_id(item_id):
    # return the data from retrieve_data()
    return jsonify(retrieve_data()[int(item_id) - 1])

# run the app
if __name__ == '__main__':
    app.run(debug=True)

