from flask import Flask, jsonify
from flask_cors import CORS
#Change this to __init__ to other machines can easily run the server
import sys
#Adding the path to the sys path
sys.path.insert(0, r"\Users\jakep\OneDrive\Desktop\Projects\Loan_Approval\backend\sources")
sys.path.insert(0, r"\Users\jakep\OneDrive\Desktop\Projects\Loan_Approval\backend\resources")


from runrf import train, predict




# app instance
app = Flask(__name__)
CORS(app)

#/api/home
@app.route("/api/home", methods=['GET'])
def return_home():

    df, randforest = train()
    pred = [76,0,12,360,1,1,0,1,0,0,0,1,0,0,0,1]
    result = predict(df, randforest, pred)
    return jsonify({"message": str(result[0])})

if __name__ == "__main__":
    app.run(debug=True, port=8080)