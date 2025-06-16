"""
File : enderecotipoDAO.py

Function : Metodos de manuseio de registros no banco de dados para a tabela de Cadastro de Tipos de Endereço (TB04002)

Author: Sidney Sanches Moreira

Object DataBase: Table TB04002
"""
import dao
import log



class EnderecoTipoDAO(dao.Dao):

    def __init__(self):
        super().__init__("TB04002", "Tipo", "o", "Cadastro de Tipos de Endereço",
                         "S", "S", "S", "TB04002")

    def listEnderecoTipo(self, params):
        """
        Metodo de listagem de enderecotipo tendo o título das colunas como "atributos da classe"

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

    def fieldsEnderecoTipo(self, params):
        """
        Metodo de listagem de enderecotipo tendo o titulo das colunas como "nome dos campos"

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

    def dictEnderecoTipo(self, params):
        """
        Metodo de listagem de enderecotipo tendo o titulo das colunas como "descrição dos campos"

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

    def findEnderecoTipo(self, params):
        """
        Metodo para que procurar um enderecotipo em específico

        :param params: JSON - Onde precisa ser passados os seguintes valores:

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON -> EnderecoTipo
        """
        try:
            return super().find(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def enderecotipoID(self, params):
        """
        Metodo que gera o último codigo de enderecotipo

        :param params: JSON com o token do acesso ao banco de dados.
        :return: Str -> Novo Código
        """
        try:
            return log.geralog(0, "OK", super().getID(params))
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def insEnderecoTipo(self, params):
        """
        Metodo onde insere EnderecoTipo no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().insert(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def updEnderecoTipo(self, params):
        """
        Metodo onde altera EnderecoTipo no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().update(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def delEnderecoTipo(self, params):
        """
        Metodo onde exclui EnderecoTipo no banco de dados.
        :param params: JSON - Valores
        :return: JSON
        """
        try:
            return super().delete(params)
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
