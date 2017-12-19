import os
from flask import Flask
from dotenv import load_dotenv,find_dotenv
app = Flask(__name__)

load_dotenv(find_dotenv())

@app.route('/')
def hello():
    return "Hello World!"
@app.route('/name')
def name():
	return os.environ.get("SECRET_KEY")


if __name__ == '__main__':
    app.run()

