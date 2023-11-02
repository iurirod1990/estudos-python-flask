"""este código demonstra a estrutura basica de um programa flask"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Olá, mundo!"

app.run(debug = True)