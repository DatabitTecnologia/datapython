"""
File : orcamentoparcelaDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de Parcelas de Orçamentos (TB02098)

Author: Sidney Sanches Moreira

Object DataBase: Table TB02098
"""
import dao
import log


class OrcamentoParcelaDAO(dao.Dao):

    def __init__(self):
        super().__init__( "TB02098", "Parcela", "a",
                         "Parcelas de Orçamentos", "N", "N", "S", "VW02084")

    def listOrcamentoParcela(self, params):
        """
        Metodo de listagem de orcamentoparcela tendo o título das colunas como "atributos da classe"

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

    def fieldsOrcamentoParcela(self, params):
        """
        Metodo de listagem de orcamentoparcela tendo o titulo das colunas como "nome dos campos"

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

    def dictOrcamentoParcela(self, params):
        """
        Metodo de listagem de orcamentoparcela tendo o titulo das colunas como "descrição dos campos"

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

    def findOrcamentoParcela(self, params):
        """
        Metodo para que procurar um orcamentoparcela em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> OrcamentoParcela
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def orcamentoparcelaID(self, params):
        """
        Metodo que gera o último codigo de orcamentoparcela

        :param params: JSON com o token do acesso ao banco de dados.
        :return: Str -> Novo Código
        """
        try:
            return log.geralog(0, "OK", super().getID(params))
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def insOrcamentoParcela(self, params):
        """
        Metodo onde insere OrcamentoParcela no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().insert(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def updOrcamentoParcela(self, params):
        """
        Metodo onde altera OrcamentoParcela no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().update(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def delOrcamentoParcela(self, params):
        """
        Metodo onde exclui OrcamentoParcela no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().delete(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
