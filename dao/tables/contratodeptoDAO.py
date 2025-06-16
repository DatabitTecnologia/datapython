"""
File : contratodeptoDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de NDDigital - Departamento (TB02177)

Author: Sidney Sanches Moreira

Object DataBase: Table TB02177
"""
import dao
import log



class ContratoDeptoDAO(dao.Dao):

    def __init__(self):
	    super().__init__( "TB02177", "Departamento", "o" , "NDDigital - Departamento", "S", "S", "S", "VW02234")
		
		
    def listContratoDepto(self, params):
        """
        Metodo de listagem de contratodepto tendo o título das colunas como "atributos da classe"

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


    def fieldsContratoDepto(self, params):
        """
        Metodo de listagem de contratodepto tendo o titulo das colunas como "nome dos campos"

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



    def dictContratoDepto(self, params):
        """
        Metodo de listagem de contratodepto tendo o titulo das colunas como "descrição dos campos"

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


    def findContratoDepto(self, params):
        """
        Metodo para que procurar um contratodepto em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> ContratoDepto
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")



    def contratodeptoID(self, params):
        """
        Metodo que gera o último codigo de contratodepto

        :param params: JSON com o token do acesso ao banco de dados.
        :return: Str -> Novo Código
        """
        try:
            return log.geralog(0, "OK", super().getID(params))
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


    def insContratoDepto(self, params):
        """
        Metodo onde insere ContratoDepto no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().insert(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


    def updContratoDepto(self, params):
        """
        Metodo onde altera ContratoDepto no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().update(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


    def delContratoDepto(self, params):
        """
        Metodo onde exclui ContratoDepto no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().delete(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


