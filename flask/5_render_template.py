'''vamos demosntrar como renderizar templates
em vez de ficar colocando o codigo html no meio do codigo python'''

from flask import Flask, render_template




app = Flask(__name__)

@app.route("/saudar/<nome>")
def saudar(nome):
    return render_template("saudar.html", nome = nome)

if __name__ == "__main__":
    app.run(debug=True)
