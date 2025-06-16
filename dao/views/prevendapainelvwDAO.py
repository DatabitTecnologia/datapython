"""
File : prevendapainelvwDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de TB01006,TB01008,TB01127,TB01128,TB01156,TB01160,TB02303 (VW02321)

Author: Sidney Sanches Moreira

Object DataBase: View VW02321
"""
import dao
import log


class PrevendaPainelVWDAO(dao.Dao):

    def __init__(self):
        super().__init__("VW02321", "Item", "o", "TB01006,TB01008,TB01127,TB01128,TB01156,TB01160,TB02303", "N", "N",
                         "N", "TB02301")

    def listPrevendaPainelVW(self, params):
        """
        Metodo de listagem de prevendapainelvw tendo o título das colunas como "atributos da classe"

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

    def fieldsPrevendaPainelVW(self, params):
        """
        Metodo de listagem de prevendapainelvw tendo o titulo das colunas como "nome dos campos"

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

    def dictPrevendaPainelVW(self, params):
        """
        Metodo de listagem de prevendapainelvw tendo o titulo das colunas como "descrição dos campos"

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

    def findPrevendaPainelVW(self, params):
        """
        Metodo para que procurar um prevendapainelvw em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> PrevendaPainelVW
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def delPrevendaPainelVW(self, params):
        """
        Metodo onde exclui PrevendaPainelVW no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().delete(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
