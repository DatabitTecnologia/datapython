"""
File : precontratoequipamentototalDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de DataClient - Definição de Equipamentos do Pré-Contrato (Totais) (TB02268)

Author: Sidney Sanches Moreira

Object DataBase: Table TB02268
"""
import dao
import log



class PrecontratoEquipamentoTotalDAO(dao.Dao):

    def __init__(self):
	    super().__init__( "TB02268", "Totalizador", "o" , "DataClient - Definição de Equipamentos do Pré-Contrato (Totais)", "N", "N", "N", "TB02268")
		
		
    def listPrecontratoEquipamentoTotal(self, params):
        """
        Metodo de listagem de precontratoequipamentototal tendo o título das colunas como "atributos da classe"

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


    def fieldsPrecontratoEquipamentoTotal(self, params):
        """
        Metodo de listagem de precontratoequipamentototal tendo o titulo das colunas como "nome dos campos"

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



    def dictPrecontratoEquipamentoTotal(self, params):
        """
        Metodo de listagem de precontratoequipamentototal tendo o titulo das colunas como "descrição dos campos"

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


    def findPrecontratoEquipamentoTotal(self, params):
        """
        Metodo para que procurar um precontratoequipamentototal em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> PrecontratoEquipamentoTotal
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")



