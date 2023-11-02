"""demonstra os metodos http com envio de formulario
por padrao o flask responde verbo GET, se outro nao for passado
"""
"""para executar a demonstracao, execute o arquivo login.html ou 
entre na url pelo navegador"""

"""antes de tudo certifique-se de que este arquivo esteja em execucao antes
de enviar o formulario do login.html"""


from flask import Flask, request, redirect, url_for


app = Flask(__name__)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        nome = request.form['nome']
        return redirect(url_for("success", nome = nome))


    else:
        #para testar mude o metodo do formulario no login,html
        #alterne entre get e post para ver diferentes resultados
        nome = request.args.get("nome")
        return f"Você foi logado corretamente {nome}, mas agora usando o método GET"

#definir funcao sucesso
@app.route("/success/<nome>")
def success(nome):
    return f"Olá {nome}, você foi logado corretamente"



if __name__ == "__main__":
    app.run(debug=True)