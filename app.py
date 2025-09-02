from flask import Flask, request, redirect
import conexao_banco, logica as logica

app = Flask(__name__)



@app.route("/")
def home():
    return conexao_banco.get_lista()

@app.route("/post", methods= ["POST"])
def link():
    data = request.json
    return logica.encurta(data)

@app.route("/get/<shorturl>", methods = ['GET'])
def visita_site(shorturl):
    url = conexao_banco.get_link(shorturl)

    if url:
        return redirect(url, code=302)
    else:
        return 'não encontrado no banco'