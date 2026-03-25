# app.py - A simple Flask API
# Flask is a lightweight web framework for Python

# --- STEP 1: Import Flask ---
# "from flask import Flask" brings in the Flask class we need
from flask import jsonify, Flask

# --- STEP 2: Create the app ---
# Flask(__name__) creates a new Flask application
# __name__ tells Flask where to find your project files
app = Flask(__name__)

# --- STEP 3: Define a route ---
# @app.route("/health") maps the URL "/health" to the function below
# When someone visits http://localhost:5000/health, this function runs
@app.route("/health")
def health():
    # jsonify() converts a Python dictionary into a JSON response
    return jsonify({"message": "Hello World"})

# --- STEP 4: Run the app ---
# This block only runs when you execute "python3 app.py" directly
# debug=True auto-reloads the server when you change code (useful while learning)
if __name__ == "__main__":
    # Starts the server on http://localhost:5000
    app.run(debug=True)
