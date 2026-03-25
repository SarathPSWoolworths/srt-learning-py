# app.py - A simple Flask API
# Flask is a lightweight web framework for Python

# --- STEP 1: Import Flask ---
# "from flask import Flask" brings in the Flask class we need
from flask import Flask, jsonify, request
from flask_cors import CORS

# --- STEP 2: Create the app ---
# Flask(__name__) creates a new Flask application
# __name__ is a special Python variable ("dunder name").
# Dunder means double underscores before and after a name.
# Python sets __name__ automatically for every module.
# Flask uses it to locate project resources correctly.
app = Flask(__name__)

# Allow CORS only for Angular dev server running on localhost:4200.
CORS(app, resources={r"/*": {"origins": ["http://localhost:4200"]}})

# --- STEP 3: Define a route ---
# @app.route("/health") maps the URL "/health" to the function below
# When someone visits http://localhost:5000/health, this function runs
@app.route("/health")
def health():
    # jsonify() converts a Python dictionary into a JSON response
    # 200 is the HTTP status code for "OK"
    return jsonify({"message": "Hello World"}), 200

# This route catches all other URLs that are not defined above.
@app.route("/<path:path>")
def catch_all(path):
    # jsonify() converts a Python dictionary into a JSON response
    # 404 is the HTTP status code for "Not Found"
    return jsonify({"Error": "Path Not Found: " + path}), 404

# This route demonstrates how to read GET query params and POST payload values.
@app.route("/args", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # Read key/value pairs from the URL query string, for example: /args?name=sam
        query_params = request.args.to_dict(flat=True)
        return (
            jsonify({"message": "Received query parameters", "params": query_params}),
            200,
        )

    # Read JSON body for requests sent as application/json.
    json_body = request.get_json(silent=True) or {}
    # Read form fields for requests sent as
    # application/x-www-form-urlencoded or multipart/form-data.
    form_body = request.form.to_dict(flat=True)
    # Return both so you can see which POST format the client used.
    return (
        jsonify({"message": "Received POST values", "json": json_body, "form": form_body}),
        200,
    )

# --- STEP 4: Run the app ---
# This block only runs when you execute "python3 app.py" directly
# debug=True auto-reloads the server when you change code (useful while learning)
if __name__ == "__main__":
    # "__main__" is the module name Python gives to the entry script.
    # So this condition is True only when this file is run directly.
    # If this file is imported from another file, this block will not run.
    # Starts the server on http://localhost:5000
    app.run(debug=True)
