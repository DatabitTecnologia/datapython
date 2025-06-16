"""
File : oportunidadeworkflowvwDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de TB01129,TB01130 (VW01126)

Author: Sidney Sanches Moreira

Object DataBase: View VW01126
"""
import dao
import log


class OportunidadeWorkflowVWDAO(dao.Dao):

    def __init__(self):
        super().__init__("VW01126", "Status", "o", "TB01129,TB01130", "N", "N", "S", "TB01130")

    def listOportunidadeWorkflowVW(self, params):
        """
        Metodo de listagem de oportunidadeworkflowvw tendo o título das colunas como "atributos da classe"

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

    def fieldsOportunidadeWorkflowVW(self, params):
        """
        Metodo de listagem de oportunidadeworkflowvw tendo o titulo das colunas como "nome dos campos"

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

    def dictOportunidadeWorkflowVW(self, params):
        """
        Metodo de listagem de oportunidadeworkflowvw tendo o titulo das colunas como "descrição dos campos"

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

    def findOportunidadeWorkflowVW(self, params):
        """
        Metodo para que procurar um oportunidadeworkflowvw em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> OportunidadeWorkflowVW
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
