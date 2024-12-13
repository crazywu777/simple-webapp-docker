import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome V2!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you? V2'

if __name__ == "__main__":
    app.run()
