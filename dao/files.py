import connect
import pandas as pd
import log
import base64


class Files:
    def getFile(self, params):
        try:
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])
            try:
                table = df_params.loc["table", 0]
            except:
                table = ""

            try:
                fieldpk = df_params.loc["fieldpk", 0]
            except:
                fieldpk = ""

            try:
                field = df_params.loc["field", 0]
            except:
                field = ""

            try:
                value = df_params.loc["value", 0]
            except:
                value = ""

            ssql = "SELECT REPLACE(REPLACE((SELECT CAST({} as VARBINARY(MAX)) as ARQ " \
                   "FROM {} WHERE {} = '{}' FOR XML  PATH(''), BINARY BASE64)," \
                   "'<ARQ>',''),'</ARQ>','') AS arq;".format(field, table, fieldpk, value)

            dados_picture = connect.dataconnect(stoken, 0)
            cursor_picture = dados_picture.cursor()
            cursor_picture.execute(ssql)
            valores_lista = cursor_picture.fetchall()
            descricao_lista = cursor_picture.description
            colunas_lista = [tp[0] for tp in descricao_lista]
            tabela_lista = pd.DataFrame.from_records(valores_lista, columns=colunas_lista)
            tabela_lista.head()
            cursor_picture.close()
            dados_picture.close()
            sJson = tabela_lista.to_json(orient="records")
            return sJson
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def setFile(self, params):
        try:
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])
            try:
                table = df_params.loc["table", 0]
            except:
                table = ""

            try:
                fieldpk = df_params.loc["fieldpk", 0]
            except:
                fieldpk = ""

            try:
                field = df_params.loc["field", 0]
            except:
                field = ""

            try:
                value = df_params.loc["value", 0]
            except:
                value = ""

            try:
                img64 = df_params.loc["base64", 0]
            except:
                img64 = ""

            hexstr = str(base64.b64decode(img64).hex())
            hexstr = "0x" + hexstr.replace("'", "")

            ssql = "UPDATE {} SET {} = {}" \
                   " WHERE {} = '{}' ".format(table, field, hexstr, fieldpk, value)

            dados_picture = connect.dataconnect(stoken, 0)
            cursor_picture = dados_picture.cursor()
            cursor_picture.execute(ssql)
            cursor_picture.commit()
            return log.geralog(1, "OK", "Arquivo salvo com Sucesso !")
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
