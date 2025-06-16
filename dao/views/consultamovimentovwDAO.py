"""
File : consultamovimentovwDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de TB01006,TB01008,TB01014,TB01021,TB01022,TB01156,TB01160,TB02018,TB02021,TB02303 (VW02322)

Author: Sidney Sanches Moreira

Object DataBase: View VW02322
"""
import dao
import log


class ConsultaMovimentoVWDAO(dao.Dao):

    def __init__(self):
        super().__init__("VW02322", "Movimento", "o",
                         "TB01006,TB01008,TB01014,TB01021,TB01022,TB01156,TB01160,TB02018,TB02021,TB02303", "N", "N",
                         "N", "TB02303")

    def listConsultaMovimentoVW(self, params):
        """
        Metodo de listagem de consultamovimentovw tendo o título das colunas como "atributos da classe"

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

    def fieldsConsultaMovimentoVW(self, params):
        """
        Metodo de listagem de consultamovimentovw tendo o titulo das colunas como "nome dos campos"

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

    def dictConsultaMovimentoVW(self, params):
        """
        Metodo de listagem de consultamovimentovw tendo o titulo das colunas como "descrição dos campos"

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

    def findConsultaMovimentoVW(self, params):
        """
        Metodo para que procurar um consultamovimentovw em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> ConsultaMovimentoVW
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
