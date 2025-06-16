"""
File : log.py

Function : Criação de recurso de geração de LOG de retorno do banco de dados via JSON

Author: Sidney Sanches Moreira
"""
import json

def geralog(istatus: object, ssituacao: object, smensagem: object) -> object:
    """
    Método para gerar LOG de retorno formato JSON

    :rtype: object
    :param istatus: Código de Status (-1 = Erro, 0 = Advertência, 1 = OK)
    :param ssituacao: Situação de Ocorreu
    :param smensagem: Mensagem apresentada ao usuário
    :return: JSON
    """
    sdict = {"status": istatus, "situacao": ssituacao, "mensagem": smensagem.replace("'", " ")}
    sjson = json.dumps(sdict)
    return sjson

