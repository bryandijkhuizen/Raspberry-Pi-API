# import Flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# create Flask app
app = Flask(__name__)

# create a main route
@app.route('/')
def index():
    return 'Hello, World!'

# create a 'post' route to send data to the server


# run the app
if __name__ == '__main__':
    app.run(debug=True)

