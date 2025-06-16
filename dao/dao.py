"""
File : dao.py

Function : Métodos de tratamento de persistência ao banco de dados.

Author: Sidney Sanches Moreira
"""

import json
from collections import namedtuple
from datetime import datetime

import pandas as pd
import log
from sqlalchemy.ext.declarative import DeclarativeMeta

from codigo import addcodigo
import connect
from threading import Thread


def jsonDecoder(jsondict):
    """
     Metodo de conversão de JSON para Objeto (Classe)

     :param jsondict: Dicionário (JSON)

     :return: Object
     """
    return namedtuple('X', jsondict.keys())(*jsondict.values())


def jsontoObject(params):
    """
    Método que pega os valores de um JSON e migra para objeto, para jogar no banco de dados.

    :param params: Informações dos valores de cada atributo.

    :return: Object
    """
    sobj = params
    sobj = json.dumps(sobj, indent=2, cls=jsonEncoder)
    objfim = json.loads(sobj, object_hook=jsonDecoder)
    return objfim


class Dao:

    def __init__(self, tabela, termo, genero, titulo, autoincremento, nameexists, foreign, tableref):
        self.tabela = tabela
        self.termo = termo
        self.genero = genero
        self.titulo = titulo
        self.autoincremento = autoincremento
        self.nameexists = nameexists
        self.foreing = foreign
        self.tableref = tableref

    def listagem(self, params, idicionario):
        """
        Método que realiza a listagem de registros em formato JSON buscando do banco de dados

        token: Token de conexão ao banco de dados

        tabela: Tabela ou view do banco de dados que deseja realizar a pesquisa

        filtro: Qual é o critério de filtro que está sendo feita a listagem, podendo também, colocar o tanto 'order by',
        quanto 'group by', neste parametro

        campos: Quais seriam os campos (colunas) que desejam ser retornados na pesquisa

        dicionario: Qual será os títulos das colunas (0 - Atribuitos da classe, 1 - Campos da tabela, 2 - Descrição dos
        campos)


        :param params: JSON onde define o método do filtro desejado:
        :param idicionario: Onde define o tipo nomenclatura dos atributos da classe (1 - "atributos da classe", 2 - "nome dos campos", 3 - "descrição dos campos")

        :return: JSON
        """
        try:
            # Atibuindo os parâmetros nas variaveis
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])

            try:
                stabela = df_params.loc["tabela", 0]
            except Exception:
                stabela = str(self.tabela).replace("(", "").replace(")", "").replace(",", "").replace("'", "")

            try:
                scampos = str(df_params.loc["campos", 0])
            except Exception:
                scampos = "*"

            try:
                scamposcalc = str(df_params.loc["camposcalc", 0])
            except Exception:
                scamposcalc = ""

            try:
                sfiltros = str(df_params.loc["filtro", 0])
            except Exception:
                sfiltros = " 0 = 0 "

            try:
                icount = int(df_params.loc["count", 0])
            except Exception:
                icount = 0

            try:
                joinuser = bool(df_params.loc["joinuser", 0])
            except Exception:
                joinuser = False

            try:
                primarykey = str(df_params.loc["primarykey", 0])
            except Exception:
                primarykey = ""

            if idicionario == 0:
                stermo = " ' as ' + '''' + CASE WHEN CHARINDEX('_',B.COLUMN_NAME) > 0 THEN LOWER(SUBSTRING(B.COLUMN_NAME,9,50)) ELSE LOWER(B.COLUMN_NAME) END + '''' "
            elif idicionario == 1:
                stermo = "' as ' + '''' + B.COLUMN_NAME + ''''  "
            else:
                stermo = " ' as ' + '''' + CAST(C.VALUE AS VARCHAR(200)) + '''' "

            scamposcomhora = "TB02257_DATA,TB02257_PREVISAO,TB02266_DATA,TB00111_DTENV,TB02115_DATA,TB02115_DTFECHA,TIME,TB02130_DATA,TB02302_DATA,TB02306_DATA,TB02130_DATA"

            sfield = " CASE WHEN CHARINDEX('numeric',B.DATA_TYPE) > 0 THEN CAST(B.COLUMN_NAME AS VARCHAR(50))  " \
                     "      WHEN CHARINDEX('datetime',B.DATA_TYPE) > 0 THEN " \
                     " 			 CASE WHEN (CHARINDEX('DTCAD',B.COLUMN_NAME) = 0 AND CHARINDEX('DTALT',B.COLUMN_NAME) = 0) AND CHARINDEX(B.COLUMN_NAME,'{}') = 0 " \
                     "      		  THEN 'convert(varchar(20),'+B.COLUMN_NAME+',103)' " \
                     "      		  ELSE 'convert(varchar(20),'+B.COLUMN_NAME+',103)+'' ''+convert(varchar(20),'+B.COLUMN_NAME+',108)'  " \
                     " 		     END " \
                     "      ELSE CAST(B.COLUMN_NAME AS VARCHAR(50)) " \
                     " END ".format(scamposcomhora)

            if stabela[0:2] == "TB":
                sqlcampos = "SELECT distinct STRING_AGG(CAST({} + {} AS VARCHAR(MAX)),',') as sql," \
                            "STRING_AGG(CAST(CAST(B.COLUMN_NAME AS VARCHAR(50)) AS VARCHAR(MAX)),',') as campos, isnull(i.is_primary_key, 0) as pk " \
                            "FROM  SYS.TABLES A " \
                            "LEFT JOIN INFORMATION_SCHEMA.COLUMNS B ON (A.NAME = B.TABLE_NAME) " \
                            "LEFT JOIN SYS.EXTENDED_PROPERTIES C ON (A.OBJECT_ID = C.MAJOR_ID AND B.ORDINAL_POSITION = C.MINOR_ID) " \
                            "left join sys.index_columns ic on ic.column_id = B.ORDINAL_POSITION and ic.object_id = a.object_id " \
                            "left join sys.indexes i on i.index_id = ic.index_id and ic.object_id = i.object_id " \
                            " WHERE A.NAME = '{}' ".format(sfield, stermo, stabela)
            else:
                sqlcampos = "SELECT distinct STRING_AGG(CAST({} + {} AS VARCHAR(MAX)),',') as sql," \
                            "STRING_AGG(CAST(CAST(B.COLUMN_NAME AS VARCHAR(50)) AS VARCHAR(MAX)),',') as campos, isnull(i.is_primary_key, 0) as pk " \
                            "FROM SYS.VIEWS A " \
                            "LEFT JOIN INFORMATION_SCHEMA.COLUMNS B ON (A.NAME = B.TABLE_NAME) " \
                            "LEFT JOIN SYS.COLUMNS D ON (B.COLUMN_NAME = D.NAME) " \
                            "LEFT JOIN SYS.EXTENDED_PROPERTIES C ON (D.OBJECT_ID = C.MAJOR_ID  AND D.COLUMN_ID = C.MINOR_ID) " \
                            "left join sys.index_columns ic on ic.column_id = B.ORDINAL_POSITION and ic.object_id = d.object_id " \
                            "left join sys.indexes i on i.index_id = ic.index_id and ic.object_id = i.object_id ".format(
                    sfield, stermo)

                if joinuser:
                    sqlcampos += "WHERE (A.NAME = '{}' or A.NAME = '{}_USER') and d.is_identity = 0 and D.object_id = a.object_id ".format(
                        stabela, stabela)
                else:
                    sqlcampos += "WHERE A.NAME = '{}' and d.is_identity = 0 and D.object_id = a.object_id ".format(
                        stabela)

            if (scampos != "") and (scampos != "*"):
                sqlcampos = sqlcampos + " AND (CHARINDEX(B.COLUMN_NAME,'{}') > 0 ".format(
                    scampos) + " or isnull(i.is_primary_key, 0) = 1)"

            sqlcampos = sqlcampos + " AND B.DATA_TYPE <> 'image' AND B.DATA_TYPE <> 'varbinary' "

            sqlcampos = sqlcampos + " group by isnull(i.is_primary_key, 0) order by 3 desc "

            # Criando conexão com o Banco de Dados
            dados_lista = connect.dataconnect(stoken, 0)
            cursor_lista = dados_lista.cursor()
            cursor_campos = dados_lista.cursor()

            cursor_campos.execute(sqlcampos)
            valores_campos = cursor_campos.fetchall()
            descricao_campos = cursor_campos.description
            colunas_campos = [tp[0] for tp in descricao_campos]
            tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
            sqlchaves = tabela_campos["sql"][0]
            schaves = tabela_campos["campos"][0]
            try:
                sqlcampos = tabela_campos["sql"][1]
            except:
                sqlcampos = tabela_campos["sql"][0]
                listcampos = schaves.split(",")
                schaves = listcampos[0]
                sqlchaves = ""

            if scamposcalc != "":
                sqlcampos = sqlcampos + "," + scamposcalc

            scount = ""
            if icount > 0:
                scount = "TOP {}".format(str(icount))

            sqlcamposfim = sqlcampos

            sfrom = " from " + stabela + " WITH (NOLOCK) "
            if joinuser and stabela[0:2] != "TB":
                sfrom += " left join {}_USER on (".format(stabela)
                listprimary = primarykey.split(",")
                for scampo in listprimary:
                    sfrom += "{}.{} = {}_USER.{}_USER and ".format(stabela, scampo, stabela, scampo)
                sfrom = sfrom[:-5] + ")"

            if sqlchaves != "":
                if "ORDER BY" not in sfiltros.upper():
                    ssql = "select " + scount + " row_number() over (order by " + schaves + " asc) - 1 as id, " + sqlchaves + "," + sqlcamposfim + " {} where ".format(
                        sfrom) + sfiltros
                else:
                    ipos = sfiltros.upper().find("ORDER BY")
                    sordem = sfiltros[ipos + 8:len(sfiltros)].strip()
                    ssql = "select " + scount + " row_number() over (order by " + sordem + " ) - 1 as id, " + sqlchaves + "," + sqlcamposfim + " {} where ".format(
                        sfrom) + sfiltros
            else:
                if "ORDER BY" not in sfiltros.upper():
                    ssql = "select " + scount + " row_number() over (order by " + schaves + " asc) - 1 as id, " + sqlcamposfim + " {} where ".format(
                        sfrom) + sfiltros
                else:
                    ipos = sfiltros.upper().find("ORDER BY")
                    sordem = sfiltros[ipos + 8:len(sfiltros)].strip()
                    ssql = "select " + scount + " row_number() over (order by " + sordem + " ) - 1 as id, " + sqlcamposfim + " {} where ".format(
                        sfrom) + sfiltros


            cursor_lista.execute(ssql)
            valores_lista = cursor_lista.fetchall()
            descricao_lista = cursor_lista.description
            colunas_lista = [tp[0] for tp in descricao_lista]
            tabela_lista = pd.DataFrame.from_records(valores_lista, columns=colunas_lista)
            tabela_lista.head()
            # Fechando Conexões
            cursor_lista.close()
            dados_lista.close()
            return tabela_lista.to_json(orient="records")

        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def find(self, params):
        """
        Método para que procurar um objeto em específico, onde é necessário ser passados os seguintes valores:

        :param params: JSON

        token: Token da Databit (Obrigatório)

        filtro: Filtro desejaddo (Opcional)

        campos: Quais seriam os campos (colunas) que desejam ser retornados na pesquisa (Opcional)

        ordem: Ordem do resultado da pesquisa (Opcional)

        :return: JSON
        """
        try:
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])

            try:
                sfiltro = str(df_params.loc["filtro", 0])
            except Exception:
                sfiltro = ""

            try:
                sordem = str(df_params.loc["ordem", 0])
            except Exception:
                sordem = ""

            try:
                scampos = str(df_params.loc["campos", 0])
            except Exception:
                scampos = "*"

            try:
                scamposcalc = str(df_params.loc["camposcalc", 0])
            except Exception:
                scamposcalc = ""

            scamposcomhora = "TB02257_DATA,TB02257_PREVISAO,TB02266_DATA,TB00111_DTENV,TB02115_DATA,TB02115_DTFECHA"
            if self.tabela[0:2] == "TB":
                sfield = "CASE WHEN CHARINDEX('datetime', A.DATA_TYPE) = 0 THEN CAST(A.COLUMN_NAME AS VARCHAR(50)) " \
                         "ELSE " \
                         " CASE WHEN (CHARINDEX('DTCAD',A.COLUMN_NAME) = 0 AND CHARINDEX('DTALT',A.COLUMN_NAME) = 0) and CHARINDEX(A.COLUMN_NAME,'{}') = 0 " \
                         "      THEN 'convert(varchar(20),'+A.COLUMN_NAME+',103) as '+substring(A.COLUMN_NAME,9,50) " \
                         "      ELSE 'convert(varchar(20),'+A.COLUMN_NAME+',103)+'' ''+convert(varchar(20),'+A.COLUMN_NAME+',108) as '+substring(A.COLUMN_NAME,9,50)" \
                         " END " \
                         "END ".format(scamposcomhora)
                sqlcampos = "select LOWER(STRING_AGG({},';')) as campos_table, " \
                            " '' as campos_view, " \
                            "LOWER(STRING_AGG(CASE WHEN ISNULL(OBJECTPROPERTY(OBJECT_ID(D.constraint_name), 'IsPrimaryKey'),0) > 0 THEN A.COLUMN_NAME ELSE NULL END,',')) as pk " \
                            "from INFORMATION_SCHEMA.COLUMNS AS A " \
                            "LEFT JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS D ON (D.COLUMN_NAME = A.COLUMN_NAME AND D.TABLE_NAME = '{}' and ISNULL(OBJECTPROPERTY(OBJECT_ID(D.constraint_name), 'IsPrimaryKey'),0) > 0) " \
                            "WHERE A.TABLE_NAME = '{}' ".format(sfield, self.tabela, self.tabela)
            else:
                sfield = "CASE WHEN CHARINDEX('datetime', A.DATA_TYPE) = 0 THEN CAST(A.COLUMN_NAME AS VARCHAR(50)) " \
                         "ELSE " \
                         " CASE WHEN (CHARINDEX('DTCAD',A.COLUMN_NAME) = 0 AND CHARINDEX('DTALT',A.COLUMN_NAME) = 0) and CHARINDEX(A.COLUMN_NAME,'{}') = 0 " \
                         "      THEN 'convert(varchar(20),'+A.COLUMN_NAME+',103) as '+A.COLUMN_NAME " \
                         "      ELSE 'convert(varchar(20),'+A.COLUMN_NAME+',103)+'' ''+convert(varchar(20),'+A.COLUMN_NAME+',108) as '+A.COLUMN_NAME" \
                         " END " \
                         "END ".format(scamposcomhora)
                sqlcampos = "select LOWER(STRING_AGG(CASE WHEN charindex('{}',A.COLUMN_NAME) > 0 THEN {} ELSE NULL END,';')) as campos_table, " \
                            " LOWER(STRING_AGG(CASE WHEN charindex('{}',A.COLUMN_NAME) = 0 THEN {} ELSE NULL END,',')) as campos_view, " \
                            "LOWER(STRING_AGG(CASE WHEN ISNULL(OBJECTPROPERTY(OBJECT_ID(D.constraint_name), 'IsPrimaryKey'),0) > 0 THEN A.COLUMN_NAME ELSE NULL END,',')) as pk " \
                            "from INFORMATION_SCHEMA.COLUMNS AS A " \
                            "LEFT JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS D ON (D.COLUMN_NAME = A.COLUMN_NAME AND D.TABLE_NAME = '{}' and ISNULL(OBJECTPROPERTY(OBJECT_ID(D.constraint_name), 'IsPrimaryKey'),0) > 0) " \
                            "WHERE A.TABLE_NAME = '{}' ".format(self.tableref, sfield, self.tableref, sfield,
                                                                self.tableref,
                                                                self.tabela)

            if scampos != "*":
                sqlcampos = sqlcampos + " AND CHARINDEX(A.COLUMN_NAME,'{}') > 0 ".format(scampos)

            sqlcampos = sqlcampos + " AND A.DATA_TYPE <> 'image' AND  A.DATA_TYPE <> 'varbinary' "

            dados_lista = connect.dataconnect(stoken, 0)
            cursor_campos = dados_lista.cursor()
            cursor_campos.execute(sqlcampos)
            valores_campos = cursor_campos.fetchall()
            descricao_campos = cursor_campos.description
            colunas_campos = [tp[0] for tp in descricao_campos]
            tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
            scampostabela = tabela_campos["campos_table"][0]
            scamposview = tabela_campos["campos_view"][0]

            sSQLSelect = "SELECT TOP 1 "

            if scampostabela is not None:
                listCampos = scampostabela.split(';')
                for campo in listCampos:
                    if "convert" not in campo:
                        sSQLSelect = sSQLSelect + "{} as '{}',".format(campo, campo[8:])
                    else:
                        sSQLSelect = sSQLSelect + "{},".format(campo)

            if (scamposview != "") and (scamposview is not None):
                sSQLSelect = sSQLSelect + scamposview
            else:
                sSQLSelect = sSQLSelect[:-1]

            if scamposcalc != "":
                sSQLSelect = sSQLSelect + "," + scamposcalc

            sSQLSelect = sSQLSelect + " FROM {}  WITH (NOLOCK) ".format(self.tabela)
            if sfiltro != "":
                sSQLSelect = sSQLSelect + " WHERE {} ".format(sfiltro)
            if sordem != "":
                sSQLSelect = sSQLSelect + " ORDER BY {} ".format(sordem)



            cursor_campos.execute(sSQLSelect)
            valores_lista = cursor_campos.fetchall()
            descricao_lista = cursor_campos.description
            colunas_lista = [tp[0] for tp in descricao_lista]
            tabela_lista = pd.DataFrame.from_records(valores_lista, columns=colunas_lista)
            tabela_lista.head()
            cursor_campos.close()
            dados_lista.close()
            sJson = tabela_lista.to_json(orient="records")
            sJson = sJson.replace("[", "")
            sJson = sJson.replace("]", "")
            return sJson
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def findObj(self, stoken, filtro):

        sfield = "CASE WHEN CHARINDEX('datetime', DATA_TYPE) = 0 THEN CAST(COLUMN_NAME AS VARCHAR(50)) " \
                 "ELSE " \
                 " CASE WHEN CHARINDEX('DTCAD',COLUMN_NAME) = 0 AND CHARINDEX('DTALT',COLUMN_NAME) = 0 " \
                 "      THEN 'convert(varchar(20),'+COLUMN_NAME+',103) as '+substring(COLUMN_NAME,9,50) " \
                 "      ELSE 'convert(varchar(20),'+COLUMN_NAME+',103)+'' ''+convert(varchar(20),'+COLUMN_NAME+',108) as '+substring(COLUMN_NAME,9,50)" \
                 " END " \
                 "END "

        sqlcampos = "select LOWER(STRING_AGG({},';')) as campos from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME  = '{}' ".format(
            sfield,
            self.tabela)

        sqlcampos = sqlcampos + " AND DATA_TYPE <> 'image'  AND  DATA_TYPE <> 'varbinary' "

        dados_lista = connect.dataconnect(stoken, 0)
        cursor_campos = dados_lista.cursor()
        cursor_campos.execute(sqlcampos)
        valores_campos = cursor_campos.fetchall()
        descricao_campos = cursor_campos.description
        colunas_campos = [tp[0] for tp in descricao_campos]
        tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
        scampostabela = tabela_campos["campos"][0]

        sSQLSelect = "SELECT TOP 1 "

        listCampos = scampostabela.split(';')
        for campo in listCampos:
            if "convert" not in campo:
                sSQLSelect = sSQLSelect + "{} as '{}',".format(campo, campo[8:])
            else:
                sSQLSelect = sSQLSelect + "{},".format(campo)

        sSQLSelect = sSQLSelect[:-1]
        sSQLSelect = sSQLSelect + " FROM {} ".format(self.tabela)
        sSQLSelect = sSQLSelect + " WHERE {} ".format(filtro)

        cursor_campos.execute(sSQLSelect)
        valores_lista = cursor_campos.fetchall()
        descricao_lista = cursor_campos.description
        colunas_lista = [tp[0] for tp in descricao_lista]
        tabela_lista = pd.DataFrame.from_records(valores_lista, columns=colunas_lista)

        sJson = tabela_lista.to_json(orient="records")
        sJson = sJson.replace("[", "")
        sJson = sJson.replace("]", "")
        objresult = jsontoObject(sJson)

        tabela_lista.head()
        cursor_campos.close()
        dados_lista.close()

        return objresult

    def findKey(self, stoken, obj):

        dados_lista = connect.dataconnect(stoken, 0)
        cursor_campos = dados_lista.cursor()

        ssqlcampos = "SELECT A.COLUMN_NAME AS campo, A.DATA_TYPE AS tipo, LOWER(SUBSTRING(A.COLUMN_NAME,9,50)) as nome FROM  INFORMATION_SCHEMA.COLUMNS AS A " \
                     "INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS D ON (D.COLUMN_NAME = A.COLUMN_NAME AND D.TABLE_NAME = '{}' and ISNULL(OBJECTPROPERTY(OBJECT_ID(D.constraint_name), 'IsPrimaryKey'),0) > 0) " \
                     "LEFT JOIN SYS.TABLES B ON B.NAME = A.TABLE_NAME " \
                     "LEFT JOIN SYS.EXTENDED_PROPERTIES C ON (B.OBJECT_ID = C.MAJOR_ID  AND A.ORDINAL_POSITION = C.MINOR_ID) " \
                     "WHERE A.TABLE_NAME = '{}' ".format(self.tabela, self.tabela)

        ssqlcampos = ssqlcampos + " AND A.DATA_TYPE <> 'image'  AND  A.DATA_TYPE <> 'varbinary'  "
        cursor_campos.execute(ssqlcampos)

        valores_campos = cursor_campos.fetchall()
        descricao_campos = cursor_campos.description
        colunas_campos = [tp[0] for tp in descricao_campos]
        tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
        tabela_campos.head()

        swhere = "0 = 0 "
        for i, j in tabela_campos.iterrows():
            scampo = j["campo"]
            snome = j["nome"]
            stipo = j["tipo"]
            if "datetime" in stipo:
                swhere += " and {} = '{}' ".format(scampo,
                                                   datetime.date.strftime(getattr(obj, snome), "%m/%d/%Y"))
            elif "char" in stipo:
                swhere += " and {} = '{}' ".format(scampo, getattr(obj, snome))
            elif "numeric" in stipo or "int" in stipo:
                swhere += " and {} = {} ".format(scampo, getattr(obj, snome))

        objfim = self.findObj(stoken, swhere)
        return objfim

    def isExists(self, dados_exists, tabela, filtro):

        sqlfiltro = " SELECT 1 FROM {} WHERE {} ".format(tabela, filtro)
        cursor_exists = dados_exists.cursor()
        cursor_exists.execute(sqlfiltro)
        valores_campos = cursor_exists.fetchall()
        descricao_campos = cursor_exists.description
        colunas_campos = [tp[0] for tp in descricao_campos]
        tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
        tabela_campos.head()
        iquant = tabela_campos[tabela_campos.columns[0]].count()
        cursor_exists.close()

        return iquant > 0

    def getID(self, params):
        """
        Método que retorna o ultimo código de uma tabela

        :param params: JSON com o token do acesso ao banco de dados.
        :return: Str -> Novo Código
        """
        scodigo = ""
        if self.autoincremento == "S" and self.tabela != "TB00035":
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])

            stabela = str(self.tabela).replace("(", "").replace(")", "").replace(",", "").replace("'", "")

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
                              "WHERE A.TABLE_NAME = '{}' ".format(self.tabela, self.tabela)

                cursor_contador.execute(sqlcontador)
                valores_campos = cursor_contador.fetchall()
                descricao_campos = cursor_contador.description
                colunas_campos = [tp[0] for tp in descricao_campos]
                tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
                itamanho = tabela_campos["tamanho"][0]
                scodigo = ("0" * itamanho)

                sqlcontador = "INSERT INTO TB00002(TB00002_COD,TB00002_NOME,TB00002_TABELA,TB00002_TAMANHO) values ('{}','{}','{}','{}')".format(
                    scodigo, self.titulo, self.tabela, itamanho)
                cursor_contador.execute(sqlcontador)
                cursor_contador.commit()

            if stabela not in "TB02018,TB02021":
                staberef = self.tabela
            else:
                staberef = 'TB00000'

            scodigo = addcodigo(scodigo)
            while self.isExists(dados_contador, staberef, " {}_CODIGO = '{}'".format(staberef, scodigo)):
                scodigo = addcodigo(scodigo)

            sqlcontador = "UPDATE TB00002 SET TB00002_COD = '{}' WHERE TB00002_TABELA = '{}'".format(scodigo,
                                                                                                     self.tabela)
            cursor_contador.execute(sqlcontador)
            cursor_contador.commit()

            cursor_contador.close()
            dados_contador.close()

        return scodigo

    def nameExists(self, dados, scodigo, snome):
        """
        Método de verificação que já existe um item com a mesma descrição

        :param session: Sessão de transaçao do banco de dados.
        :param scodigo: Código do cadastro, quando se trata de inclusão, preencher com None
        :param snome: Descrição para ser verificada

        :return: Boolean
        """
        if self.nameexists == "S":

            sfiltro = "select {}_CODIGO as codigo from {} where ".format(self.tabela, self.tabela)
            sfiltro += "{}_NOME = '{}' ".format(self.tabela, snome)
            if scodigo is not None:
                sfiltro += " and {}_CODIGO <> '{}' ".format(self.tabela, scodigo)

            cursor_exists = dados.cursor()
            cursor_exists.execute(sfiltro)
            valores_campos = cursor_exists.fetchall()
            descricao_exists = cursor_exists.description
            colunas_exists = [tp[0] for tp in descricao_exists]
            tabela_exists = pd.DataFrame.from_records(valores_campos, columns=colunas_exists)
            tabela_exists.head()
            iquant = tabela_exists[tabela_exists.columns[0]].count()
            cursor_exists.close()
            if iquant > 0:
                scodigofim = tabela_exists["codigo"][0]
                return scodigofim
            else:
                return None
        else:
            return None

    def foreingKeys(self, stoken, scodigo):
        """
        Método onde verifica se o registro que está sendo excluído, possui alguma restrição de chave estrangeira
        :param stoken: Token de conexão
        :param scodigo: Código do item
        :return: JSON
        """
        dados_chaves = connect.dataconnect(stoken, 0)
        cursor_chaves = dados_chaves.cursor()
        ssqlchaves = "exec SP00000 '{}','{}' ".format(self.tabela, scodigo)
        cursor_chaves.execute(ssqlchaves)
        valores_chaves = cursor_chaves.fetchall()
        descricao_chaves = cursor_chaves.description
        colunas_chaves = [tp[0] for tp in descricao_chaves]
        tabela_chaves = pd.DataFrame.from_records(valores_chaves, columns=colunas_chaves)
        tabela_chaves.head()
        iquant = tabela_chaves[tabela_chaves.columns[0]].count()
        if iquant == 0:
            cursor_chaves.close()
            dados_chaves.close()
            return "OK"
        else:
            stabelas = ""
            for i, j in tabela_chaves.iterrows():
                sdescricao = j["NOME"]
                iquant = j["QUANT"]
                stabelas = stabelas + sdescricao + " : " + str(iquant) + " registro(s), "

            sdic = {"status": 0, "situacao": "Aviso",
                    "mensagem": "Não é possivel excluir este registro, pois possuem referências nas tabelas : {}".format(
                        stabelas)}

            jsonString = json.dumps(sdic, indent=2)
            cursor_chaves.close()
            dados_chaves.close()
            return jsonString

    def updateRegistrador(self, stoken, scodigo, susuario, objant, objnovo):
        """
        Método para registrar as alterações realizadas no registro
        :param stoken: Token de conexão
        :param scodigo: Códido do movimento
        :param susuario: Usuário
        :param objant: Objeto anterior
        :param objnovo: Objeto atual
        :return: None
        """
        dados_update = connect.dataconnect(stoken, 0)
        cursor_update = dados_update.cursor()
        ssqlupdate = "exec SP07001 '{}','{}','{}','{}','{}' ".format(scodigo, self.tabela, susuario,
                                                                     objant, objnovo)
        cursor_update.execute(ssqlupdate)
        cursor_update.close()
        dados_update.commit()
        dados_update.close()
        return

    def deleteRegistrador(self, stoken, scodigo, susuario, obj):
        """
        Método para registrar as exclusões realizadas
        :param stoken: Token de conexão
        :param scodigo: Códido do movimento
        :param susuario: Usuário
        :param obj: Objeto que foi excluído
        :return: None
        """
        dados_delete = connect.dataconnect(stoken, 0)
        cursor_delete = dados_delete.cursor()
        ssqldelete = "exec SP07002 '{}','{}','{}','{}' ".format(scodigo, self.tabela, susuario, obj)
        cursor_delete.execute(ssqldelete)
        cursor_delete.close()
        dados_delete.commit()
        dados_delete.close()

    def insert(self, params):
        """
        Método de inserção de registros no banco de dados.

        :param params: Token, Usuário e a Classe em formato JSON
        :return: JSON
        """
        try:

            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])
            susuario = str(df_params.loc["usuario", 0])
            objfim = jsontoObject(df_params.loc["object", 0])
            scodigo = ""
            sqlcampos = "select distinct LOWER(STRING_AGG(SUBSTRING(A.COLUMN_NAME,9,50),';')) as campos from INFORMATION_SCHEMA.COLUMNS as A " \
                        "left join sys.all_columns on sys.all_columns.name = A.COLUMN_NAME  " \
                        "left join sys.tables on sys.tables.name = A.TABLE_NAME " \
                        " WHERE  A.TABLE_NAME = '{}' AND sys.all_columns.is_computed = 0 AND sys.all_columns.is_identity = 0 and sys.tables.object_id = sys.all_columns.object_id ".format(
                self.tabela)
            sqlcampos = sqlcampos + " AND A.DATA_TYPE <> 'image'  AND  A.DATA_TYPE <> 'varbinary'  "

            dados_insert = connect.dataconnect(stoken, 0)
            cursor_campos = dados_insert.cursor()
            cursor_campos.execute(sqlcampos)
            valores_campos = cursor_campos.fetchall()
            descricao_campos = cursor_campos.description
            colunas_campos = [tp[0] for tp in descricao_campos]
            tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
            scampostabela = ';' + tabela_campos["campos"][0] + ';'

            if ("nome" in scampostabela) and (hasattr(objfim, 'nome')) and (self.nameexists == "S"):
                if getattr(objfim, "nome") == "" or getattr(objfim, "nome") is None:
                    return log.geralog(0, "Aviso",
                                       "Descrição d{} {} é de preenchimento obrigatório !".format(self.genero,
                                                                                                  self.termo))
                if "codigo" in scampostabela:
                    existe = self.nameExists(dados_insert, None, getattr(objfim, "nome"))
                    if existe is not None:
                        cursor_campos.close()
                        dados_insert.close()
                        return log.geralog(0, "Aviso",
                                           "Descrição d{} {} já existente".format(self.genero, self.termo),
                                           existe)

            if (hasattr(objfim, 'codigo')) and (self.autoincremento == "S"):
                scodigo = getattr(objfim, "codigo")
                while self.isExists(dados_insert, self.tabela, " {}_CODIGO = '{}'".format(self.tabela, scodigo)):
                    scodigo = addcodigo(scodigo)

            sSQLInsert = "INSERT INTO {} (".format(self.tabela)
            sSQLValues = " VALUES ("

            if self.autoincremento == "S" and not (hasattr(objfim, 'codigo')) and (self.tabela != "TB00035"):
                scodigo = self.getID(params)
                sSQLInsert = sSQLInsert + "{}_CODIGO,".format(self.tabela)
                sSQLValues = sSQLValues + "'{}',".format(scodigo)
            if "dtcad" in scampostabela:
                sSQLInsert = sSQLInsert + "{}_DTCAD,".format(self.tabela)
                sSQLValues = sSQLValues + "getdate(),"
            if "opcad" in scampostabela:
                sSQLInsert = sSQLInsert + "{}_OPCAD,".format(self.tabela)
                sSQLValues = sSQLValues + "'{}',".format(susuario)

            campos_inclusao = dir(objfim)
            campos_inclusao = filter(lambda x: ("_" not in x), campos_inclusao)
            campos_inclusao = list(campos_inclusao)
            for i in range(len(campos_inclusao)):
                scampoinclusao = campos_inclusao[i]
                if (scampoinclusao == "id") and not (hasattr(objfim, 'codigo')):
                    scodigo = getattr(objfim, scampoinclusao)
                elif scampoinclusao == "codigo":
                    scodigo = getattr(objfim, scampoinclusao)
                if ";" + scampoinclusao + ';' in scampostabela and format(getattr(objfim, scampoinclusao)) != "" and format(
                        getattr(objfim, scampoinclusao)) is not None and format(
                    getattr(objfim, scampoinclusao)) != "None" and format(
                    getattr(objfim, scampoinclusao)) != "null":
                    valorins = str(getattr(objfim, scampoinclusao))
                    if (scampoinclusao == "codigo") and (self.autoincremento == "S"):
                        while self.isExists(dados_insert, self.tabela,
                                            " {}_CODIGO = '{}'".format(self.tabela, scodigo)):
                            scodigo = addcodigo(scodigo)
                        valorins = scodigo
                    if scampoinclusao != "dtcad" and scampoinclusao != "opcad" and scampoinclusao != "dtalt" and scampoinclusao != "opalt":
                        valorins = valorins.replace("'", "''")
                        sSQLInsert = sSQLInsert + "{}_{},".format(self.tabela, scampoinclusao.upper())
                        sSQLValues = sSQLValues + "'{}',".format(valorins)

            sSQLInsert = sSQLInsert[:-1] + ")"
            sSQLValues = sSQLValues[:-1] + ")"
            sSQLExecute = sSQLInsert + sSQLValues
            cursor_execute = dados_insert.cursor()

            cursor_execute.execute(sSQLExecute)
            cursor_execute.commit()
            cursor_execute.close()
            cursor_campos.close()
            dados_insert.close()

            return log.geralog(1, "OK", "{} {} cadastrad{} com sucesso!".format(self.termo, scodigo, self.genero),
                               scodigo)

        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def update(self, params):
        """
        Método de alteração de registros no banco de dados.

        :param params: Token, Usuário e a Classe em formato JSON
        :return: JSON
        """

        try:
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])
            susuario = str(df_params.loc["usuario", 0])
            objfim = jsontoObject(df_params.loc["object", 0])

            cledicaoant = self.findKey(stoken, objfim)
            print(objfim)
            scodigo = ""
            sqlcampos = "select LOWER(STRING_AGG(substring(A.COLUMN_NAME,9,50),';')) as campos, " \
                        "LOWER(STRING_AGG(CASE WHEN ISNULL(OBJECTPROPERTY(OBJECT_ID(D.constraint_name), 'IsPrimaryKey'),0) > 0 THEN A.COLUMN_NAME ELSE NULL END,';')) as pk," \
                        "STRING_AGG(case when sys.all_columns.is_identity = 1 then LOWER(substring(A.COLUMN_NAME,9,50)) else '' end,',') as ids " \
                        "from INFORMATION_SCHEMA.COLUMNS AS A " \
                        "LEFT JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS D ON (D.COLUMN_NAME = A.COLUMN_NAME AND D.TABLE_NAME = '{}' and ISNULL(OBJECTPROPERTY(OBJECT_ID(D.constraint_name), 'IsPrimaryKey'),0) > 0) " \
                        "left join sys.all_columns on sys.all_columns.name = A.COLUMN_NAME   " \
                        "left join sys.tables on sys.tables.name = A.TABLE_NAME " \
                        "WHERE A.TABLE_NAME = '{}' AND sys.all_columns.is_computed = 0 AND  sys.tables.object_id = sys.all_columns.object_id  ".format(
                self.tabela,
                self.tabela)

            dados_update = connect.dataconnect(stoken, 0)
            cursor_campos = dados_update.cursor()
            sqlcampos = sqlcampos + " AND DATA_TYPE <> 'image'  AND  DATA_TYPE <> 'varbinary'  "
            cursor_campos.execute(sqlcampos)
            print(sqlcampos)
            valores_campos = cursor_campos.fetchall()
            descricao_campos = cursor_campos.description
            colunas_campos = [tp[0] for tp in descricao_campos]
            tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
            scampostabela = ';' + tabela_campos["campos"][0] + ';'
            scampospk =tabela_campos["pk"][0] + ';'
            sidentity = tabela_campos["ids"][0]

            if ("nome" in scampostabela) and (hasattr(objfim, 'nome')) and (self.nameexists == "S"):
                if getattr(objfim, "nome") == "" or getattr(objfim, "nome") is None:
                    return log.geralog(0, "Aviso",
                                       "Descrição d{} {} é de preenchimento obrigatório !".format(self.genero,
                                                                                                  self.termo))
                if "codigo" in scampostabela:
                    existe = self.nameExists(dados_update, getattr(objfim, "codigo"), getattr(objfim, "nome"))
                    if existe is not None:
                        cursor_campos.close()
                        dados_update.close()
                        return log.geralog(0, "Aviso",
                                           "Descrição d{} {} já existente".format(self.genero, self.termo),
                                           existe)

            sSQLUpdate = "UPDATE {} ".format(self.tabela) + " SET "

            if "dtalt" in scampostabela:
                sSQLUpdate = sSQLUpdate + "{}_DTALT = getdate(),".format(self.tabela)
            if "opalt" in scampostabela:
                sSQLUpdate = sSQLUpdate + "{}_OPALT = '{}',".format(self.tabela, susuario)

            campos_edicao = dir(objfim)
            campos_edicao = filter(lambda x: ("_" not in x), campos_edicao)
            campos_edicao = list(campos_edicao)
            for i in range(len(campos_edicao)):
                scampoedicao = campos_edicao[i]
                if scampoedicao not in sidentity:
                    if scampoedicao == "codigo":
                        scodigo = getattr(objfim, scampoedicao)
                    if ";" + scampoedicao + ';' in scampostabela and format(
                            getattr(objfim, scampoedicao)) is not None and format(
                        getattr(objfim, scampoedicao)) != "None" and format(getattr(objfim, scampoedicao)) != "null":
                        valorupd = str(getattr(objfim, scampoedicao))
                        valorupd = valorupd.replace("'", "''")
                        if scampoedicao != "dtcad" and scampoedicao != "opcad" and scampoedicao != "dtalt" and scampoedicao != "opalt":
                            if valorupd != "" and valorupd is not None:
                                sSQLUpdate = sSQLUpdate + "{}_{} = '{}',".format(self.tabela, scampoedicao.upper(),
                                                                                 valorupd)
                            else:
                                sSQLUpdate = sSQLUpdate + "{}_{} = NULL,".format(self.tabela, scampoedicao.upper())

            sSQLUpdate = sSQLUpdate[:-1]
            sSQLWhere = " where "


            for i in range(len(campos_edicao)):
                scampoedicao = campos_edicao[i]
                scampofim = self.tabela + '_' + scampoedicao
                if scampofim.upper() + ';' in scampospk.upper() and format(
                        getattr(objfim, scampoedicao)) != "" and format(
                    getattr(objfim, scampoedicao)) is not None and format(
                    getattr(objfim, scampoedicao)) != "None" and format(getattr(objfim, scampoedicao)) != "null":
                    sSQLWhere = sSQLWhere + "{}_{} = '{}' and ".format(self.tabela, scampoedicao.upper(),
                                                                       getattr(objfim, scampoedicao))

            sSQLWhere = sSQLWhere[:-5]
            sSQLExecute = sSQLUpdate + sSQLWhere

            cursor_execute = dados_update.cursor()
            print(sSQLExecute)
            cursor_execute.execute(sSQLExecute)

            cursor_execute.commit()
            cursor_execute.close()
            cursor_campos.close()
            dados_update.close()

            cledicaofim = self.findKey(stoken, objfim)

            new_thread = Thread(target=self.updateRegistrador,
                                args=(stoken, scodigo, susuario, cledicaoant, cledicaofim))
            new_thread.start()

            return log.geralog(1, "OK", "{} {} alterad{} com sucesso!".format(self.termo, scodigo, self.genero),
                               scodigo)

        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def delete(self, params):
        """
        Método de exclusão de registros no banco de dados.

        :param params: Token, Usuário e a Classe em formato JSON
        :return: JSON
        """
        try:
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])
            susuario = str(df_params.loc["usuario", 0])
            objfim = jsontoObject(df_params.loc["object", 0])
            clsexclusao = self.findKey(stoken, objfim)
            scodigo = ""
            sqlcampos = "select LOWER(STRING_AGG(A.COLUMN_NAME,';')) as campos, " \
                        "LOWER(STRING_AGG(CASE WHEN ISNULL(OBJECTPROPERTY(OBJECT_ID(D.constraint_name), 'IsPrimaryKey'),0) > 0 THEN A.COLUMN_NAME ELSE NULL END,';')) as pk " \
                        "from INFORMATION_SCHEMA.COLUMNS AS A " \
                        "INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS D ON (D.COLUMN_NAME = A.COLUMN_NAME AND D.TABLE_NAME = '{}' and ISNULL(OBJECTPROPERTY(OBJECT_ID(D.constraint_name), 'IsPrimaryKey'),0) > 0) " \
                        "WHERE A.TABLE_NAME = '{}' ".format(self.tabela, self.tabela)

            dados_delete = connect.dataconnect(stoken, 0)
            cursor_campos = dados_delete.cursor()
            sqlcampos = sqlcampos + " AND DATA_TYPE <> 'image'  AND DATA_TYPE <> 'varbinary'  "
            cursor_campos.execute(sqlcampos)
            valores_campos = cursor_campos.fetchall()
            descricao_campos = cursor_campos.description
            colunas_campos = [tp[0] for tp in descricao_campos]
            tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
            scampospk = tabela_campos["pk"][0] + ';'
            if self.tabela == "TB00012":
                scampospk = "tabela;tipo;codigo"

            if clsexclusao is not None:
                if self.foreing == "S":
                    if hasattr(objfim, 'codigo'):
                        sretorno = self.foreingKeys(stoken, getattr(objfim, "codigo"))
                    else:
                        sretorno = "OK"
                else:
                    sretorno = "OK"
                if sretorno == "OK":

                    sSQLDelete = "DELETE FROM {} where ".format(self.tabela)

                    campos_exclusao = dir(objfim)
                    campos_exclusao = filter(lambda x: ("_" not in x), campos_exclusao)
                    campos_exclusao = list(campos_exclusao)
                    for i in range(len(campos_exclusao)):
                        scampoexclusao = campos_exclusao[i]
                        if scampoexclusao == "codigo":
                            scodigo = getattr(objfim, scampoexclusao)
                        scampofim = self.tabela + '_' + scampoexclusao
                        if scampofim.upper() + ';' in scampospk.upper() and format(
                                getattr(objfim, scampoexclusao)) != "" and format(
                            getattr(objfim, scampoexclusao)) is not None and format(
                            getattr(objfim, scampoexclusao)) != "None" and format(
                            getattr(objfim, scampoexclusao)) != "null":
                            sSQLDelete = sSQLDelete + "{}_{} = '{}' and ".format(self.tabela, scampoexclusao.upper(),
                                                                                 getattr(objfim, scampoexclusao))

                    sSQLDelete = sSQLDelete[:-5]
                    cursor_execute = dados_delete.cursor()

                    cursor_execute.execute(sSQLDelete)

                    cursor_execute.commit()
                    cursor_execute.close()
                    cursor_campos.close()
                    dados_delete.close()

                    new_thread = Thread(target=self.deleteRegistrador,
                                        args=(stoken, scodigo, susuario, clsexclusao))
                    new_thread.start()

                    return log.geralog(1, "OK",
                                       "{} {} excluíd{} com sucesso!".format(self.termo, scodigo,
                                                                             self.genero), scodigo)
                else:
                    return sretorno
            else:
                return log.geralog(0, "Aviso",
                                   "{} não existente, ou já excluid{} anteriormente!".format(self.termo, self.genero))
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")


class jsonEncoder(json.JSONEncoder):
    """
    Function: Classe de migração de Objeto para JSON
    """

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    stipo = str(type(data))
                    if "datetime" in stipo:
                        sdata = str(data)
                        sdia = sdata[8:10]
                        smes = sdata[5:7]
                        sano = sdata[0:4]
                        shora = sdata[11:19]
                        sdata = sdia + "/" + smes + "/" + sano + " " + shora
                        json.dumps(sdata.strip())
                        fields[field] = sdata.strip()
                    else:
                        json.dumps(str(data))
                        fields[field] = str(data)
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)
