"""
File : log.py

Function : Criação de recurso de geração de LOG de retorno do banco de dados via JSON

Author: Sidney Sanches Moreira
"""
import json


def geralog(istatus: object, ssituacao: object, smensagem: object, sid: object = 0) -> object:
    """
    Método para gerar LOG de retorno formato JSON

    :param sid: ID de retorno do Objeto
    :rtype: object
    :param istatus: Código de Status (-1 = Erro, 0 = Advertência, 1 = OK)
    :param ssituacao: Situação de Ocorreu
    :param smensagem: Mensagem apresentada ao usuário
    :return: JSON
    """
    sdict = {"id": sid, "status": istatus, "situacao": ssituacao, "mensagem": smensagem.replace("'", " ")}
    sjson = json.dumps(sdict)
    return sjson

