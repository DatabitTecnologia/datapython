"""
File : condicaodescontooperacaoDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de Listagem de desconto (Condicao de Recebimento) (TB01026)

Author: Sidney Sanches Moreira

Object DataBase: Table TB01026
"""
import dao
import log


class CondicaoDescontoOperacaoDAO(dao.Dao):

    def __init__(self):
        super().__init__("TB01026", "Desconto", "o", "Listagem de desconto (Condicao de Recebimento)", "N", "N", "S",
                         "TB01026")

    def listCondicaoDescontoOperacao(self, params):
        """
        Metodo de listagem de condicaodescontooperacao tendo o título das colunas como "atributos da classe"

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

    def fieldsCondicaoDescontoOperacao(self, params):
        """
        Metodo de listagem de condicaodescontooperacao tendo o titulo das colunas como "nome dos campos"

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

    def dictCondicaoDescontoOperacao(self, params):
        """
        Metodo de listagem de condicaodescontooperacao tendo o titulo das colunas como "descrição dos campos"

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

    def findCondicaoDescontoOperacao(self, params):
        """
        Metodo para que procurar um condicaodescontooperacao em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> CondicaoDescontoOperacao
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def insCondicaoDescontoOperacao(self, params):
        """
        Metodo onde insere CondicaoDescontoOperacao no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().insert(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def updCondicaoDescontoOperacao(self, params):
        """
        Metodo onde altera CondicaoDescontoOperacao no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().update(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def delCondicaoDescontoOperacao(self, params):
        """
        Metodo onde exclui CondicaoDescontoOperacao no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().delete(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
