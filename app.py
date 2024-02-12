import random
from flask import Flask, jsonify

app = Flask(__name__)
from quotes import quotes
import gunicorn
@app.get("/")
def welcome_text():
    return {"Text":"Witamy w StopTheBluesAPI!"}

@app.get("/randomQuote")
def get_random_quote():
    return quotes[random.randint(0,10)]

if __name__ == "__main__":
    app.run()