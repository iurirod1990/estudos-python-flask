'''os arquivos estaticos do app flask devem ficar dentro da
pasta static (js, css etc)'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home_demonstrate_static.html")


if __name__ == "__main__":
    app.run(debug= True)