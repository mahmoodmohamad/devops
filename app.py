from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)

# Define the version of the app
APP_VERSION = "v0.0.1"

# Define route for the /version endpoint
@app.route('/version')
def get_version():
    """
    Returns the version of the deployed app.
    """
    return jsonify({"version": APP_VERSION})

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
