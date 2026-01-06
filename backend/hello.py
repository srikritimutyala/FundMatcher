print("Python is running!")

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "Flask works!"}

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
