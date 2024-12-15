from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask import request

app = Flask(__name__)
application = app

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False, port=8000)
