from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! This app was made without certain packages in the requirements.txt" 

if __name__ == "__main__":
    import bjoern

    bjoern.run(app, "127.0.0.1", 8000)
