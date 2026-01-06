from flask import Flask
from flask_cors import CORS

# Import your blueprints
from routes.profiles import profiles_bp
from routes.match import match_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(profiles_bp)
app.register_blueprint(match_bp)

@app.route("/")
def home():
    return {"status": "FundMatcher backend running"}

print("Before running Flask...")

if __name__ == "__main__":
    print("Starting FundMatcher backend...")
    app.run(debug=True)
