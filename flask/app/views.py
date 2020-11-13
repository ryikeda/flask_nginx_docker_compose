from app import app

@app.route("/")
def index():
    return "Hello from Flask"

@app.route("/name/<name>")
def hello(name):
    return f"Welcome {name}!"

