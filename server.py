from flask import Flask, send_from_directory
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    # esegue sync.py ad ogni apertura/refresh
    subprocess.run(["python", "sync.py"])
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    app.run(debug=True, port=8000)