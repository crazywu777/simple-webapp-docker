import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome V3!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you? V3'

if __name__ == "__main__":
    app.run()
