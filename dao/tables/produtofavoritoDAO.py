"""
File : produtofavoritoDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de Produtos Favoritos (WEB) (TB01164)

Author: Sidney Sanches Moreira

Object DataBase: Table TB01164
"""
import dao
import log


class ProdutoFavoritoDAO(dao.Dao):

    def __init__(self):
        super().__init__("TB01164", "Produto", "o", "Produtos Favoritos (WEB)", "N", "N", "N", "TB01164")

    def listProdutoFavorito(self, params):
        """
        Metodo de listagem de produtofavorito tendo o título das colunas como "atributos da classe"

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

    def fieldsProdutoFavorito(self, params):
        """
        Metodo de listagem de produtofavorito tendo o titulo das colunas como "nome dos campos"

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

    def dictProdutoFavorito(self, params):
        """
        Metodo de listagem de produtofavorito tendo o titulo das colunas como "descrição dos campos"

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

    def findProdutoFavorito(self, params):
        """
        Metodo para que procurar um produtofavorito em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> ProdutoFavorito
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def insProdutoFavorito(self, params):
        """
        Metodo onde insere ProdutoFavorito no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().insert(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def updProdutoFavorito(self, params):
        """
        Metodo onde altera ProdutoFavorito no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().update(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def delProdutoFavorito(self, params):
        """
        Metodo onde exclui ProdutoFavorito no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().delete(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
