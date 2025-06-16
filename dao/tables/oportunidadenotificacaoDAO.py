"""
File : oportunidadenotificacaoDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de DataClient - Status de Oportunidades (Notificação de Usuários) (TB01143)

Author: Sidney Sanches Moreira

Object DataBase: Table TB01143
"""
import dao
import log



class OportunidadeNotificacaoDAO(dao.Dao):

    def __init__(self):
	    super().__init__( "TB01143", "Usuário", "o" , "DataClient - Status de Oportunidades (Notificação de Usuários)", "N", "N", "N", "TB01143")
		
		
    def listOportunidadeNotificacao(self, params):
        """
        Metodo de listagem de oportunidadenotificacao tendo o título das colunas como "atributos da classe"

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


    def fieldsOportunidadeNotificacao(self, params):
        """
        Metodo de listagem de oportunidadenotificacao tendo o titulo das colunas como "nome dos campos"

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



    def dictOportunidadeNotificacao(self, params):
        """
        Metodo de listagem de oportunidadenotificacao tendo o titulo das colunas como "descrição dos campos"

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


    def findOportunidadeNotificacao(self, params):
        """
        Metodo para que procurar um oportunidadenotificacao em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> OportunidadeNotificacao
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")



    def insOportunidadeNotificacao(self, params):
        """
        Metodo onde insere OportunidadeNotificacao no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().insert(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


    def updOportunidadeNotificacao(self, params):
        """
        Metodo onde altera OportunidadeNotificacao no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().update(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


    def delOportunidadeNotificacao(self, params):
        """
        Metodo onde exclui OportunidadeNotificacao no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().delete(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


