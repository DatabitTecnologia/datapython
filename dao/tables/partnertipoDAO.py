"""
File : partnertipoDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de DataPartner - Tipos de Solicitação de Compras (TB01152)

Author: Sidney Sanches Moreira

Object DataBase: Table TB01152
"""
import dao
import log


class PartnerTipoDAO(dao.Dao):

    def __init__(self):
        super().__init__("TB01152", "Tipo", "o", "DataPartner - Tipos de Solicitação de Compras", "S", "S", "S",
                         "TB01152")

    def listPartnerTipo(self, params):
        """
        Metodo de listagem de partnertipo tendo o título das colunas como "atributos da classe"

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

    def fieldsPartnerTipo(self, params):
        """
        Metodo de listagem de partnertipo tendo o titulo das colunas como "nome dos campos"

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

    def dictPartnerTipo(self, params):
        """
        Metodo de listagem de partnertipo tendo o titulo das colunas como "descrição dos campos"

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

    def findPartnerTipo(self, params):
        """
        Metodo para que procurar um partnertipo em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> PartnerTipo
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def partnertipoID(self, params):
        """
        Metodo que gera o último codigo de partnertipo

        :param params: JSON com o token do acesso ao banco de dados.
        :return: Str -> Novo Código
        """
        try:
            return log.geralog(0, "OK", super().getID(params))
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def insPartnerTipo(self, params):
        """
        Metodo onde insere PartnerTipo no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().insert(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def updPartnerTipo(self, params):
        """
        Metodo onde altera PartnerTipo no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().update(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def delPartnerTipo(self, params):
        """
        Metodo onde exclui PartnerTipo no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().delete(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
