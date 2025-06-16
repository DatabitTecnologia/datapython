"""
File : recebervwDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de TB01006,TB01007,TB01008,TB01011,TB01014,TB01107,TB02021,TB02118,TB04003,TB04004,TB04005,TB04006,TB04008,TB04009,TB04010,TB04011,TB04013 (VW04004)

Author: Sidney Sanches Moreira

Object DataBase: View VW04004
"""
import dao
import log



class ReceberVWDAO(dao.Dao):

    def __init__(self):
	    super().__init__( "VW04004", "Conta à Receber", "a" , "TB01006,TB01007,TB01008,TB01011,TB01014,TB01107,TB02021,TB02118,TB04003,TB04004,TB04005,TB04006,TB04008,TB04009,TB04010,TB04011,TB04013", "N", "N", "N", "TB04010")
		
		
    def listReceberVW(self, params):
        """
        Metodo de listagem de recebervw tendo o título das colunas como "atributos da classe"

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


    def fieldsReceberVW(self, params):
        """
        Metodo de listagem de recebervw tendo o titulo das colunas como "nome dos campos"

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



    def dictReceberVW(self, params):
        """
        Metodo de listagem de recebervw tendo o titulo das colunas como "descrição dos campos"

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


    def findReceberVW(self, params):
        """
        Metodo para que procurar um recebervw em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> ReceberVW
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")



