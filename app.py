from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route for '/hello'
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=int("5000"), debug=True)
