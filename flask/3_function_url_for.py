"""este módulo demonstra as funcoes orl"""

from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "Você está na pagina inicial"

@app.route("/admin/")
def saudar_admin():
    return "Olá administrador, seja bem vindo"

@app.route("/guest/<nome>")
def saudar_convidado(nome):
    return f"Olá {nome}, seja muito bem vindo como nosso convidado."

@app.route("/user/<nome>")
def user(nome):
    if nome == "admin":
        return redirect(url_for("saudar_admin"))
    else:
        return redirect(url_for("saudar_convidado", nome=nome))

if __name__ == "__main__":
    app.run(debug=True)

