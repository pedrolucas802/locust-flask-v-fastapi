from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello():
    random_number = random.randint(1, 10000)
    return "Hello from Flask! -> " + str(random_number)