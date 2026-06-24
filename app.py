from flask import Flask
app = Flask(__name__)
notes = [
    "Learn Dockr & git",
    "Build Project",
    "Deploye App"
]
@app.route("/")
def home():
    return "Notes API Running!"
@app.route("/notes")
def get_notes():
    return {"notes": notes}
if __name__ == "__main__":        
    app.run(host="0.0.0.0", port=5000)