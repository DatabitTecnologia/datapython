"""
File : browseequipprovwDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de TB01008,TB01010,TB02111,TB02112,TB02176,TB02309 (VW02332)

Author: Sidney Sanches Moreira

Object DataBase: View VW02332
"""
import dao
import log


class BrowseEquipProVWDAO(dao.Dao):

    def __init__(self):
        super().__init__("VW02332", "Item", "o", "TB01008,TB01010,TB02111,TB02112,TB02176,TB02309", "N", "N", "N",
                         "TB02309")

    def listBrowseEquipProVW(self, params):
        """
        Metodo de listagem de browseequipprovw tendo o título das colunas como "atributos da classe"

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

    def fieldsBrowseEquipProVW(self, params):
        """
        Metodo de listagem de browseequipprovw tendo o titulo das colunas como "nome dos campos"

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

    def findBrowseEquipProVW(self, params):
        """
        Metodo para que procurar um browseequipprovw em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> BrowseEquipProVW
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
