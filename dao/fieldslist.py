import connect
import pandas as pd
import log


class fieldList:

    def executeList(self, params):
        try:
            # Atibuindo os parâmetros nas variaveis
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])

            try:
                stabela = df_params.loc["tabela", 0]
            except Exception:
                stabela = str(self.tabela).replace("(", "").replace(")", "").replace(",", "").replace("'", "")

            try:
                suser = df_params.loc["user", 0]
            except Exception:
                suser = str(self.user).replace("(", "").replace(")", "").replace(",", "").replace("'", "")

            try:
                extra = df_params.loc["extra", 0]
            except Exception:
                extra = str(self.extra).replace("(", "").replace(")", "").replace(",", "").replace("'", "")

            # Criando conexão com o Banco de Dados
            dados_lista = connect.dataconnect(stoken, 0)
            dados_lista.cursor()
            cursor_campos = dados_lista.cursor()

            # Buscando campos no dicionário de dados
            ssqlcampos = "select LOWER(SUBSTRING(TB00101_CAMPO,9,50)) AS namefield, TB00101_FUNCAO AS headerName, " \
                         "dbo.FS00005(isnull(TB00003_TAMANHO,10)) as width, TB00101_CAMPO as field, " \
                         "CASE TB00003_TIPO" \
                         "  WHEN 'varchar' THEN 'string' " \
                         "  WHEN 'text' THEN 'string' " \
                         "  WHEN 'char' THEN 'string' " \
                         "  WHEN 'int' THEN 'number' " \
                         "  WHEN 'numeric' THEN 'number' " \
                         "  WHEN 'bigint' THEN 'number' " \
                         "  WHEN 'datetime' THEN 'date' " \
                         "  WHEN 'smalldatetime' THEN 'date' " \
                         "END AS type, cast(1 as bit) as visible,TB00101_ORDEM as ordem, 'header-list' as headerClassName, TB00003_DECIMAL as decimal  " \
                         "FROM TB00101 " \
                         "LEFT JOIN TB00003 ON TB00003_CAMPO = TB00101_CAMPO AND TB00003_TABELA = TB00101_TABELA  " \
                         "WHERE (TB00101_TABELA = '{}' AND TB00101_USER = '{}') ".format(stabela, suser)

            if (extra is not None) and (extra != ""):
                ssqlcampos = ssqlcampos + " UNION " \
                                          "select LOWER(SUBSTRING(TB00003_CAMPO,9,50)) AS namefield, TB00003_FUNCAO AS headerName, " \
                                          "dbo.FS00005(isnull(TB00003_TAMANHO,10)) AS width, TB00003_CAMPO as field, " \
                                          "CASE TB00003_TIPO" \
                                          "  WHEN 'varchar' THEN 'string' " \
                                          "  WHEN 'text' THEN 'string' " \
                                          "  WHEN 'char' THEN 'string' " \
                                          "  WHEN 'int' THEN 'number' " \
                                          "  WHEN 'numeric' THEN 'number' " \
                                          "  WHEN 'bigint' THEN 'number' " \
                                          "  WHEN 'datetime' THEN 'date' " \
                                          "  WHEN 'smalldatetime' THEN 'date' " \
                                          "END AS type, cast(0 as bit) as visible, 999 as ordem, 'header-list' as headerClassName, TB00003_DECIMAL as decimal " \
                                          "FROM TB00003 " \
                                          "WHERE TB00003_TABELA = '{}' AND CHARINDEX(TB00003_CAMPO,'{}') > 0 " \
                                          " AND TB00003_CAMPO NOT IN (select TB00101_CAMPO FROM TB00101 where TB00101_TABELA = '{}' AND TB00101_USER = '{}')".format(
                    stabela, extra, stabela, suser)
            ssqlcampos = ssqlcampos + " ORDER BY 7 "
            print(ssqlcampos)
            cursor_campos.execute(ssqlcampos)
            valores_campos = cursor_campos.fetchall()
            descricao_campos = cursor_campos.description
            colunas_campos = [tp[0] for tp in descricao_campos]
            tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
            tabela_campos.head()
            cursor_campos.close()

            return tabela_campos.to_json(orient="records")

        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def dictList(self, params):
        try:
            # Atibuindo os parâmetros nas variaveis
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])

            try:
                stabela = df_params.loc["tabela", 0]
            except Exception:
                stabela = str(self.tabela).replace("(", "").replace(")", "").replace(",", "").replace("'", "")

            # Criando conexão com o Banco de Dados
            dados_lista = connect.dataconnect(stoken, 0)
            dados_lista.cursor()
            cursor_campos = dados_lista.cursor()

            # Buscando campos no dicionário de dados
            ssqlcampos = "SELECT TB00003_CAMPO AS value, " \
                         "TB00003_FUNCAO as label " \
                         "FROM TB00003 WHERE TB00003_TABELA = '{}' " \
                         " ORDER BY TB00003_FUNCAO ".format(stabela)
            print(ssqlcampos)
            cursor_campos.execute(ssqlcampos)
            valores_campos = cursor_campos.fetchall()
            descricao_campos = cursor_campos.description
            colunas_campos = [tp[0] for tp in descricao_campos]
            tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
            tabela_campos.head()
            cursor_campos.close()

            return tabela_campos.to_json(orient="records")

        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def browseList(self, params):
        try:
            # Atibuindo os parâmetros nas variaveis
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])

            try:
                stabela = df_params.loc["tabela", 0]
            except Exception:
                stabela = str(self.tabela).replace("(", "").replace(")", "").replace(",", "").replace("'", "")

            try:
                scampos = df_params.loc["campos", 0]
            except Exception:
                scampos = ""

            try:
                spossui = df_params.loc["possui", 0]
            except Exception:
                spossui = "S"

            # Criando conexão com o Banco de Dados
            dados_lista = connect.dataconnect(stoken, 0)
            dados_lista.cursor()
            cursor_campos = dados_lista.cursor()

            if spossui == "S":
                ssinal = ">"
            else:
                ssinal = "="

            # Buscando campos no dicionário de dados
            if stabela[0:2] == "TB":
                ssqlcampos = "select CASE WHEN CHARINDEX('_',B.COLUMN_NAME) > 0 THEN LOWER(SUBSTRING(B.COLUMN_NAME,9,50)) ELSE LOWER(B.COLUMN_NAME) END AS field, CAST(C.VALUE AS VARCHAR(200)) AS headerName, " \
                             "dbo.FS00005(isnull(B.CHARACTER_MAXIMUM_LENGTH,10)) AS width, " \
                             "CASE B.DATA_TYPE" \
                             "  WHEN 'varchar' THEN 'string' " \
                             "  WHEN 'text' THEN 'string' " \
                             "  WHEN 'char' THEN 'string' " \
                             "  WHEN 'int' THEN 'number' " \
                             "  WHEN 'numeric' THEN 'number' " \
                             "  WHEN 'bigint' THEN 'number' " \
                             "  WHEN 'datetime' THEN 'date' " \
                             "  WHEN 'smalldatetime' THEN 'date' " \
                             "END AS type, " \
                             "isnull(i.is_primary_key, 0) as pk," \
                             "ISNULL(B.CHARACTER_MAXIMUM_LENGTH,10) AS size, " \
                             "CAST(B.COLUMN_NAME AS VARCHAR(50)) as namefield," \
                             "row_number() over (order by CAST(B.COLUMN_NAME AS VARCHAR(50)) asc) as id, " \
                             "CASE WHEN CHARINDEX('_',B.COLUMN_NAME) > 0 THEN LOWER(SUBSTRING(B.COLUMN_NAME,9,50)) ELSE LOWER(B.COLUMN_NAME) END AS campo, CAST(C.VALUE AS VARCHAR(200)) AS funcao, " \
                             "ISNULL(B.CHARACTER_MAXIMUM_LENGTH,10) AS tamanho, cast(1 as int) as tipofiltro, cast('' as varchar(10)) as tabelaref, " \
                             "ISNULL((SELECT TOP 1 TB00003_TIPOOBJECT FROM TB00003 WHERE TB00003_CAMPO = CAST(B.COLUMN_NAME AS VARCHAR(50))),1) as tipoobject, " \
                             "(SELECT TOP 1 TB00003_TIPOMASCARA FROM TB00003 WHERE TB00003_CAMPO = CAST(B.COLUMN_NAME AS VARCHAR(50))) as tipomascara, " \
                             "(SELECT TOP 1 TB00003_DECIMAL FROM TB00003 WHERE TB00003_CAMPO = CAST(B.COLUMN_NAME AS VARCHAR(50))) as decimal, " \
                             "cast(0 as int) as line, cast(0 as int) as widthfield, cast('' as varchar(10)) as measure, cast(0 as int) as widthname " \
                             "FROM  SYS.TABLES A " \
                             "LEFT JOIN INFORMATION_SCHEMA.COLUMNS B ON (A.NAME = B.TABLE_NAME) " \
                             "LEFT JOIN SYS.EXTENDED_PROPERTIES C ON (A.OBJECT_ID = C.MAJOR_ID AND B.ORDINAL_POSITION = C.MINOR_ID) " \
                             "left join sys.index_columns ic on ic.column_id = B.ORDINAL_POSITION and ic.object_id = a.object_id " \
                             "left join sys.indexes i on i.index_id = ic.index_id and ic.object_id = i.object_id " \
                             "WHERE A.NAME = '{}' and C.value is not null  and B.DATA_TYPE <> 'text'  ".format(stabela)
            else:
                ssqlcampos = "select distinct CAST(B.COLUMN_NAME AS VARCHAR(50)) AS field, CAST(ISNULL(C.VALUE,B.COLUMN_NAME) AS VARCHAR(200)) AS headerName, " \
                             "dbo.FS00005(isnull(B.CHARACTER_MAXIMUM_LENGTH,10)) AS width, " \
                             "CASE B.DATA_TYPE" \
                             "  WHEN 'varchar' THEN 'string' " \
                             "  WHEN 'text' THEN 'string' " \
                             "  WHEN 'char' THEN 'string' " \
                             "  WHEN 'int' THEN 'number' " \
                             "  WHEN 'numeric' THEN 'number' " \
                             "  WHEN 'bigint' THEN 'number' " \
                             "  WHEN 'datetime' THEN 'date' " \
                             "  WHEN 'smalldatetime' THEN 'date' " \
                             "END AS type, " \
                             "isnull(i.is_primary_key, 0) as pk," \
                             "ISNULL(B.CHARACTER_MAXIMUM_LENGTH,10) AS size, " \
                             "CAST(B.COLUMN_NAME AS VARCHAR(50)) as namefield, " \
                             "d.column_id id, " \
                             "CASE WHEN CHARINDEX('_',B.COLUMN_NAME) > 0 THEN LOWER(SUBSTRING(B.COLUMN_NAME,9,50)) ELSE LOWER(B.COLUMN_NAME) END AS campo, CAST(C.VALUE AS VARCHAR(200)) AS funcao, " \
                             "ISNULL(B.CHARACTER_MAXIMUM_LENGTH,10)  AS tamanho, cast(1 as int) as tipofiltro, cast('' as varchar(10)) as tabelaref, " \
                             "ISNULL((SELECT TOP 1 TB00003_TIPOOBJECT FROM TB00003 WHERE TB00003_CAMPO = CAST(B.COLUMN_NAME AS VARCHAR(50))),1) as tipoobject, " \
                             "(SELECT TOP 1 TB00003_TIPOMASCARA FROM TB00003 WHERE TB00003_CAMPO = CAST(B.COLUMN_NAME AS VARCHAR(50))) as tipomascara, " \
                             "(SELECT TOP 1 TB00003_DECIMAL FROM TB00003 WHERE TB00003_CAMPO = CAST(B.COLUMN_NAME AS VARCHAR(50))) as decimal, " \
                             "cast(0 as int) as line, cast(0 as int) as widthfield, cast('' as varchar(10)) as measure, cast(0 as int) as widthname " \
                             "FROM SYS.VIEWS A " \
                             "LEFT JOIN INFORMATION_SCHEMA.COLUMNS B ON (A.NAME = B.TABLE_NAME) " \
                             "LEFT JOIN SYS.COLUMNS D ON (B.COLUMN_NAME = D.NAME and d.object_id = a.object_id) " \
                             "LEFT JOIN SYS.EXTENDED_PROPERTIES C ON (D.OBJECT_ID = C.MAJOR_ID  AND D.COLUMN_ID = C.MINOR_ID) " \
                             "left join sys.index_columns ic on ic.column_id = B.ORDINAL_POSITION and ic.object_id = d.object_id " \
                             "left join sys.indexes i on i.index_id = ic.index_id and ic.object_id = i.object_id " \
                             "WHERE A.NAME = '{}' and ISNULL(C.value,B.COLUMN_NAME) is not null and B.DATA_TYPE <> 'text' ".format(stabela)

            if scampos != "":
                ssqlcampos = ssqlcampos + " AND (CHARINDEX(B.COLUMN_NAME,'{}') {} 0) ".format(scampos, ssinal)

            if stabela[0:2] == "TB":
                ssqlcampos = ssqlcampos + "ORDER BY 5 DESC, 1"
            else:
                ssqlcampos = ssqlcampos + "ORDER BY d.column_id, 1"

            print(ssqlcampos)
            cursor_campos.execute(ssqlcampos)
            valores_campos = cursor_campos.fetchall()
            descricao_campos = cursor_campos.description
            colunas_campos = [tp[0] for tp in descricao_campos]
            tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
            tabela_campos.head()
            cursor_campos.close()

            return tabela_campos.to_json(orient="records")

        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")



