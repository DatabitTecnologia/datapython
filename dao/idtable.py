import connect
import pandas as pd
from codigo import addcodigo
import log


class IDTable:

    def getIDTable(self, params):

        df_params = pd.DataFrame.from_dict(params, orient="index")
        stoken = str(df_params.loc["token", 0])

        stabela = str(df_params.loc["tabela", 0])
        # Criando conexão com o Banco de Dados
        dados_contador = connect.dataconnect(stoken, 0)
        cursor_contador = dados_contador.cursor()

        sqlcontador = "select TB00002_COD as codigo from TB00002 WHERE TB00002_TABELA = '{}' ".format(stabela)

        cursor_contador.execute(sqlcontador)
        valores_campos = cursor_contador.fetchall()
        descricao_campos = cursor_contador.description
        colunas_campos = [tp[0] for tp in descricao_campos]
        tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
        tabela_campos.head()
        iquant = tabela_campos[tabela_campos.columns[0]].count()

        if iquant > 0:
            scodigo = tabela_campos["codigo"][0]
        else:
            sqlcontador = "select CHARACTER_MAXIMUM_LENGTH as tamanho " \
                          "from INFORMATION_SCHEMA.COLUMNS AS A " \
                          "inner JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS D ON (D.COLUMN_NAME = A.COLUMN_NAME AND D.TABLE_NAME = '{}' and ISNULL(OBJECTPROPERTY(OBJECT_ID(D.constraint_name), 'IsPrimaryKey'),0) > 0) " \
                          "WHERE A.TABLE_NAME = '{}' AND CHARINDEX('CODIGO',A.COLUMN_NAME) > 0 ".format(stabela[:7],
                                                                                                    stabela[:7])

            cursor_contador.execute(sqlcontador)
            valores_campos = cursor_contador.fetchall()
            descricao_campos = cursor_contador.description
            colunas_campos = [tp[0] for tp in descricao_campos]
            tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
            itamanho = tabela_campos["tamanho"][0]
            scodigo = ("0" * itamanho)

            sqlcontador = "INSERT INTO TB00002(TB00002_COD,TB00002_NOME,TB00002_TABELA,TB00002_TAMANHO) values ('{}','{}','{}','{}')".format(
                scodigo, stabela, stabela, itamanho)
            cursor_contador.execute(sqlcontador)
            cursor_contador.commit()

        staberef = stabela[:7]

        scodigo = addcodigo(scodigo)
        while self.isExists(dados_contador, staberef, " {}_CODIGO = '{}'".format(staberef, scodigo)):
            scodigo = addcodigo(scodigo)

        if stabela[:7] in "TB02018,TB02021":
            while self.isExists(dados_contador, 'TB00000', " {}_CODIGO = '{}'".format('TB00000', scodigo)):
                scodigo = addcodigo(scodigo)


        sqlcontador = "UPDATE TB00002 SET TB00002_COD = '{}' WHERE TB00002_TABELA = '{}'".format(scodigo,
                                                                                                 stabela)
        cursor_contador.execute(sqlcontador)
        cursor_contador.commit()

        cursor_contador.close()
        dados_contador.close()
        return log.geralog(1, "OK", scodigo)

    def isExists(self, dados_exists, tabela, filtro):
        sqlfiltro = " SELECT 1 FROM {} WHERE {} ".format(tabela, filtro)
        cursor_exists = dados_exists.cursor()
        cursor_exists.execute(sqlfiltro)
        valores_campos = cursor_exists.fetchall()
        descricao_campos = cursor_exists.description
        colunas_campos = [tp[0] for tp in descricao_campos]
        tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
        tabela_campos.head()
        cursor_exists.close()
