from flask import Flask

app = Flask(__name__)

#members API route
@app.route("/members")
def members():
    return "Members"


if __name__ == "__main__":
    app.run(debug=True)