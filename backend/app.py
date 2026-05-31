from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Court Case Management Backend Running"

@app.route("/status")
def status():
    return jsonify({
        "case_no": "12345",
        "status": "Pending Hearing"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)