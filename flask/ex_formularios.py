"""este exercicio vai demonstrar o envio de informacoes por
meio de formularios e tambem o objeto request"""

#use o objeto request para pegar 3 nomes de alunos por meio de um formulario
#depois em uma pagina de saudações, print uma mensagem diferente
# de saudacao para cada aluno

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/famnames")
def famnames():
    if request.method == "GET":
        nome1 = request.args.get("n1")
        nome2 = request.args.get("n2")
        nome3 = request.args.get("n3")
        return f"{nome1} <br>{nome2}<br>{nome3}"
    else:
        return "Hello world"

@app.route("/")
def home():
    return render_template("ex_formularios_home.html")

if __name__ == "__main__":
    app.run(debug=True)