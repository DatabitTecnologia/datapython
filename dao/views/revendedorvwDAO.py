"""
File : revendedorvwDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de TB00012,TB01008 (VW01153)

Author: Sidney Sanches Moreira

Object DataBase: View VW01153
"""
import dao
import log


class RevendedorVWDAO(dao.Dao):

    def __init__(self):
        super().__init__("VW01153", "Revendedor", "o", "TB00012,TB01008", "N", "N", "N", "TB01008")

    def listRevendedorVW(self, params):
        """
        Metodo de listagem de revendedorvw tendo o título das colunas como "atributos da classe"

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

    def fieldsRevendedorVW(self, params):
        """
        Metodo de listagem de revendedorvw tendo o titulo das colunas como "nome dos campos"

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

    def dictRevendedorVW(self, params):
        """
        Metodo de listagem de revendedorvw tendo o titulo das colunas como "descrição dos campos"

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

    def findRevendedorVW(self, params):
        """
        Metodo para que procurar um revendedorvw em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> RevendedorVW
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
