# import header.py
from header import *

# create Flask app
app = Flask(__name__)

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

