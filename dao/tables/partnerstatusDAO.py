"""
File : partnerstatusDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de DataPartner - Status de Solicitação de Compras (TB01148)

Author: Sidney Sanches Moreira

Object DataBase: Table TB01148
"""
import dao
import log


class PartnerStatusDAO(dao.Dao):

    def __init__(self):
        super().__init__("TB01148", "Status", "o", "DataPartner - Status de Solicitação de Compras", "S", "S", "S",
                         "TB01148")

    def listPartnerStatus(self, params):
        """
        Metodo de listagem de partnerstatus tendo o título das colunas como "atributos da classe"

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

    def fieldsPartnerStatus(self, params):
        """
        Metodo de listagem de partnerstatus tendo o titulo das colunas como "nome dos campos"

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

    def dictPartnerStatus(self, params):
        """
        Metodo de listagem de partnerstatus tendo o titulo das colunas como "descrição dos campos"

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

    def findPartnerStatus(self, params):
        """
        Metodo para que procurar um partnerstatus em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> PartnerStatus
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def partnerstatusID(self, params):
        """
        Metodo que gera o último codigo de partnerstatus

        :param params: JSON com o token do acesso ao banco de dados.
        :return: Str -> Novo Código
        """
        try:
            return log.geralog(0, "OK", super().getID(params))
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def insPartnerStatus(self, params):
        """
        Metodo onde insere PartnerStatus no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().insert(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def updPartnerStatus(self, params):
        """
        Metodo onde altera PartnerStatus no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().update(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def delPartnerStatus(self, params):
        """
        Metodo onde exclui PartnerStatus no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().delete(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
