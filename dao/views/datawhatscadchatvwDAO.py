"""
File : datawhatscadchatvwDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de TB08001,TB08010 (VW08005)

Author: Sidney Sanches Moreira

Object DataBase: View VW08005
"""
import dao
import log



class DataWhatsCadchatVWDAO(dao.Dao):

    def __init__(self):
	    super().__init__( "VW08005", "Chat", "o" , "TB08001,TB08010", "N", "N", "N", "TB08010")
		
		
    def listDataWhatsCadchatVW(self, params):
        """
        Metodo de listagem de datawhatscadchatvw tendo o título das colunas como "atributos da classe"

        token: Token de conexao ao banco de dados (Obrigatorio)

        filtro: Qual e o criterio de filtro que esta sendo feita a listagem, podendo tambem, colocar o tanto "order by"
        quanto "group by" neste parametro (Opcional)

        campos: Quais seriam os campos (colunas) que desejam ser retornados na pesquisa (Opcional)

        :param params: JSON com as informacoes de token, filtro, campos (colunas)

        :return: JSON
        """
        try:
            return super().listagem(params, 0)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


    def fieldsDataWhatsCadchatVW(self, params):
        """
        Metodo de listagem de datawhatscadchatvw tendo o titulo das colunas como "nome dos campos"

        token: Token de conexao ao banco de dados (Obrigatório)

        filtro: Qual e o critério de filtro que esta sendo feita a listagem, podendo tambem, colocar o tanto 'order by',
        quanto 'group by', neste parametro (Opcional)

        campos: Quais seriam os campos (colunas) que desejam ser retornados na pesquisa (Opcional)

        :param params: JSON com as informacoes de token, filtro, campos (colunas)

        :return: JSON
        """
        try:
            return super().listagem(params, 1)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")



    def dictDataWhatsCadchatVW(self, params):
        """
        Metodo de listagem de datawhatscadchatvw tendo o titulo das colunas como "descrição dos campos"

        token: Token de conexão ao banco de dados (Obrigatório)

        filtro: Qual e o critério de filtro que esta sendo feita a listagem, podendo tambem, colocar o tanto 'order by',
        quanto 'group by', neste parametro (Opcional)

        campos: Quais seriam os campos (colunas) que desejam ser retornados na pesquisa (Opcional)

        :param params: JSON com as informacoes de token, filtro, campos (colunas)

        :return: JSON
        """
        try:
            return super().listagem(params, 2)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


    def findDataWhatsCadchatVW(self, params):
        """
        Metodo para que procurar um datawhatscadchatvw em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> DataWhatsCadchatVW
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")



