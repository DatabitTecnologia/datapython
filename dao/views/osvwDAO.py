"""
File : osvwDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de FS02011,TB00009,TB00012,TB01003,TB01006,TB01007,TB01008,TB01010,TB01017,TB01024,TB01055,TB01066,TB01073,TB01097,TB01098,TB01107,tb02018,tb02021,TB02054,TB02111,TB02112,TB02115,TB02115,TB02122,TB02176, (VW02095)

Author: Sidney Sanches Moreira

Object DataBase: View VW02095
"""
import dao
import log


class OsVWDAO(dao.Dao):

    def __init__(self):
        super().__init__("VW02095", "Ordem de Serviço", "a",
                         "FS02011,TB00009,TB00012,TB01003,TB01006,TB01007,TB01008,TB01010,TB01017,TB01024,TB01055,TB01066,TB01073,TB01097,TB01098,TB01107,tb02018,tb02021,TB02054,TB02111,TB02112,TB02115,TB02115,TB02122,TB02176,",
                         "N", "N", "N", "TB02115")

    def listOsVW(self, params):
        """
        Metodo de listagem de osvw tendo o título das colunas como "atributos da classe"

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

    def fieldsOsVW(self, params):
        """
        Metodo de listagem de osvw tendo o titulo das colunas como "nome dos campos"

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

    def dictOsVW(self, params):
        """
        Metodo de listagem de osvw tendo o titulo das colunas como "descrição dos campos"

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

    def findOsVW(self, params):
        """
        Metodo para que procurar um osvw em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> OsVW
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
