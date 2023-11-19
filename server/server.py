from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from runrf import train, predict

# Get the directory of this script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Add the necessary relative paths to sys.path
sources_path = os.path.join(script_dir, "backend", "sources")
resources_path = os.path.join(script_dir, "backend", "resources")

sys.path.insert(0, sources_path)
sys.path.insert(0, resources_path)

# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/api/home", methods=['POST', 'GET'])
def return_home():
    if request.method == 'POST':
        df, randforest = train()
        pred = (request.form['name']).split(',')
        result = predict(df, randforest, pred)
        return jsonify({"result": result[0]})

if __name__ == "__main__":
    app.run(debug=True, port=8080)
