"""
File : connect.py

Function : Criação de uma conexão SQL Server para realização das transações.

Author: Sidney Sanches Moreira
"""
import json

import pyodbc
import base64
import requests
import crypto
import log

def dataconnect(stoken, itipo):
    """
     Método que cria uma conexão com um banco de dados SQL-Server para a ferramentas pyodbc e sqlalchemy
     :param stoken: Número do TOKEN correspondente ao banco de dados apontado pela aplicação
     :param itipo: Tipo de Conexão

     :return: pyodbc.connect
     """
    try:
        stokenfim = base64.b64decode(stoken)
        conexao = stokenfim.split()
        sinativo = crypto.dbdecrypt(conexao[6])
        scliente = crypto.dbdecrypt(conexao[0])

        if sinativo != "N":
            raise Exception(
                "Atenção, esta conexão do CNPJ {} esta inativa, favor solicitar à Databit a verificação desta "
                "conexão !".format(scliente))
        else:
            sservidor = crypto.dbdecrypt(conexao[1])
            sbanco = crypto.dbdecrypt(conexao[2])
            susuario = crypto.dbdecrypt(conexao[3])
            ssenha = crypto.dbdecrypt(conexao[4])
            sdriver = "SQL Server"
            sporta = crypto.dbdecrypt(conexao[5])

            sconexao = "Driver={};Server={};Database={};UID={};PWD={};PORT={};".format("{" + sdriver + "}", sservidor,
                                                                                       sbanco, susuario, ssenha, sporta)
            conexao = sconexao
            if itipo == 0:  # 1 = pyodbc
                dados = pyodbc.connect(conexao)
                return dados
            else:
                return sconexao
    except Exception as erro:
        return log.geralog(-1, "ERRO", f"{erro=}")


def getConnectTOKEN(stoken):
    """
    Método onde executa uma requisição GET para o método getConnectionToken da API restConnect
    :param stoken: Token desejado
    :return: json
    """
    sURL = "http://localhost:8879/restConnect.dll/datasnap/rest/tmetodos/getConnectionToken/" + stoken
    sURLRemoto = "http://databitbh.com:38879/restConnect.dll/datasnap/rest/tmetodos/getConnectionToken/" + stoken
    try:
        api = requests.get(sURL)
        jsonfim = api.json()
        if not jsonfim:
            api = requests.get(sURLRemoto)
            jsonfim = api.json()
    except Exception:
        api = requests.get(sURLRemoto)
        jsonfim = api.json()
    return jsonfim


def getConnectCNPJ(sCNPJ):
    """
    Método onde executa uma requisição GET para o método getConnectionCNPJ da API restConnect
    :param sCNPJ: CNPJ desejado
    :return: json
    """
    sURL = "http://localhost:8879/restConnect.dll/datasnap/rest/tmetodos/getConnectionCNPJ/" + sCNPJ
    sURLRemoto = "http://databitbh.com:38879/restConnect.dll/datasnap/rest/tmetodos/getConnectionCNPJ/" + sCNPJ
    try:
        api = requests.get(sURL)
        jsonfim = api.json()
        if not jsonfim:
            api = requests.get(sURLRemoto)
            jsonfim = api.json()
    except Exception:
        api = requests.get(sURLRemoto)
        jsonfim = api.json()
    return jsonfim

# if __name__ == '__main__':
#     dataconnect("NzQ1ODJBMUU2MjI4OUU2OEFGMUE3MTZCMEZFRDRCNkY3QTAyOUE4MA==")
