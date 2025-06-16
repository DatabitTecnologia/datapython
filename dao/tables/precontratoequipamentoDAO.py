"""
File : precontratoequipamentoDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de DataClient - Definição de Equipamentos do Pré-Contrato (TB02267)

Author: Sidney Sanches Moreira

Object DataBase: Table TB02267
"""
import dao
import log



class PrecontratoEquipamentoDAO(dao.Dao):

    def __init__(self):
	    super().__init__( "TB02267", "Equipamento", "o" , "DataClient - Definição de Equipamentos do Pré-Contrato", "S", "N", "S", "TB02267")
		
		
    def listPrecontratoEquipamento(self, params):
        """
        Metodo de listagem de precontratoequipamento tendo o título das colunas como "atributos da classe"

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


    def fieldsPrecontratoEquipamento(self, params):
        """
        Metodo de listagem de precontratoequipamento tendo o titulo das colunas como "nome dos campos"

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



    def dictPrecontratoEquipamento(self, params):
        """
        Metodo de listagem de precontratoequipamento tendo o titulo das colunas como "descrição dos campos"

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


    def findPrecontratoEquipamento(self, params):
        """
        Metodo para que procurar um precontratoequipamento em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> PrecontratoEquipamento
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")



    def precontratoequipamentoID(self, params):
        """
        Metodo que gera o último codigo de precontratoequipamento

        :param params: JSON com o token do acesso ao banco de dados.
        :return: Str -> Novo Código
        """
        try:
            return log.geralog(0, "OK", super().getID(params))
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


    def insPrecontratoEquipamento(self, params):
        """
        Metodo onde insere PrecontratoEquipamento no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().insert(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


    def updPrecontratoEquipamento(self, params):
        """
        Metodo onde altera PrecontratoEquipamento no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().update(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


    def delPrecontratoEquipamento(self, params):
        """
        Metodo onde exclui PrecontratoEquipamento no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().delete(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


