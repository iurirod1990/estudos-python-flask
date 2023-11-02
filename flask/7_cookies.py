"""vamos demonstrar agora como trabalhar com cookies
que sao arquivos de texto salvos no ladod o cliente para personalizar a experiencia
do user nos site
primeiro -> criar a resposta do recurso
segundo -> criar o cookie mediante o uso do dict cookie do objeto  request"""

from flask import request, Flask, render_template, make_response



app = Flask(__name__)




@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index_cookies_lesson.html", id = request.form['id'])

#rota que define o cookie
@app.route("/setcookie", methods = ['POST', 'GET'])
def setcookie():
    if request.method == "POST":
        id = request.form['id']
        #criar a resposta
        resp = make_response(render_template("lercookie.html"))
        resp.set_cookie("userID", id)
        return resp



#rota que lê o cookie
@app.route("/getcookie")
def get_cookie():
    id = request.cookies.get("userID")
    return f"logado como usuario {id}"

if __name__ == "__main__":
    app.run(debug=True)