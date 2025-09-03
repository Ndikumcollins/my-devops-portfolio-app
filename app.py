from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, World! 🚀 This app is running in a container."

@app.get("/about")
def about():
    return "This is a demo app deployed with Docker, Jenkins & AWS."

@app.get("/healthz")
def healthz():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
