#pasta templates    guarda a marcacao html a ser exibida
from flask import  Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/users")
def user():
    return render_template("users.html", nome_usuario='iury rodd')

@app.route("/saudacao", methods=['GET', 'POST'])
def saudation():
    if request.method == "POST":
        nome = request.form['nome']
        mensagem = f'ola {nome}, bem vindo ao mundo de flask'
    return render_template("saudacao.html")


if __name__ == "__main__":
    app.run(debug= True)







