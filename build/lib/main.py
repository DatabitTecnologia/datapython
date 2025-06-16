from flask import Flask, render_template, url_for

import dao
import testeclasse
import json
from flask import request


app = Flask(__name__)

a = testeclasse.Testeclasse(1, "Sidney Sanches", "04109065658")
sjson  = '{"codigo":0,"nome":"Sidney","cpf":"04109065658"}'
sjson2 = '{"codigo": 1,"nome": "Sidney Sanches","cpf": "04109065658"}'
params = [{"token": "NzQ1ODJBMUU2MjI4OUU2OEFGMUE3MTZCMEZFRDRCNkY3QTAyOUE4MA==","tabela": "TB01008","filtro":"situacao = 'A' ","dicionario":0}]

@app.route("/")
def hello_world():
    return "<p>Olá</p>"

@app.route("/teste") # CLasse para JSON
def teste():
    sjson = json.dumps(a.__dict__)
    return sjson

@app.route("/teste2") # Colunas de um JSON
def teste2():
    data = json.loads(sjson2)
    colunas = [tp for tp in data]
    return colunas

@app.route("/teste3") # Colunas de uma Classe
def teste3():
    return a.__dir__()

@app.route("/lista/", methods = ["POST"])
def lista():
    return dao.listagem(request.json)


if __name__ == "__main__":
    app.run(debug=True)