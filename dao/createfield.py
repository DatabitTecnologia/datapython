import connect
import pandas as pd
import log
import dao


class CreateField:

    def createField(self, params):
        try:
            # Atibuindo os parâmetros nas variaveis
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])
            objcampo = dao.jsontoObject(df_params.loc["object", 0])
            dados_campo = connect.dataconnect(stoken, 0)
            cursor_campo = dados_campo.cursor()

            sqlCreate = "ALTER TABLE {} ADD {}".format(getattr(objcampo, "tabela"), getattr(objcampo, "campo"))
            if getattr(objcampo, "tipo") == "varchar":
                sqlCreate += " varchar ({}) ".format(getattr(objcampo, "tamanho"))
            elif getattr(objcampo, "tipo") == "int":
                sqlCreate += " int default 0"
            elif getattr(objcampo, "tipo") == "numeric":
                sqlCreate += " numeric(20,{}) default 0".format(getattr(objcampo, "decimal"))
            else:
                sqlCreate += " {}".format(getattr(objcampo, "tipo"))
            cursor_campo.execute(sqlCreate)
            cursor_campo.commit()

            sqlDescricao = "exec sys.sp_addextendedproperty 'MS_Description','{}','SCHEMA','dbo','TABLE','{}','COLUMN','{}' ".format(
                getattr(objcampo, "funcao"),
                getattr(objcampo, "tabela"),
                getattr(objcampo, "campo"))
            cursor_campo.execute(sqlDescricao)
            cursor_campo.commit()

            try:
                if getattr(objcampo, "isforeign") == 1:
                    sqlForeign = "ALTER TABLE {} WITH CHECK ADD  CONSTRAINT {} FOREIGN KEY({}) REFERENCES {} ({}_CODIGO)".format(
                        getattr(objcampo, "tabela"),
                        getattr(objcampo, "key"),
                        getattr(objcampo, "campo"),
                        getattr(objcampo, "tabelaref"),
                        getattr(objcampo, "tabelaref"))
                    cursor_campo.execute(sqlForeign)
                    cursor_campo.commit()
            except Exception as erro:
                print(erro)

            cursor_campo.close()
            dados_campo.close()

            return log.geralog(1, "OK", "Campo '{} - {}' criado com sucesso !".format(getattr(objcampo, "campo"),
                                                                                      getattr(objcampo, "funcao")))
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")

    def updateField(self, params):
        try:
            # Atibuindo os parâmetros nas variaveis
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])
            objcampo = dao.jsontoObject(df_params.loc["object", 0])
            dados_campo = connect.dataconnect(stoken, 0)
            cursor_campo = dados_campo.cursor()

            sqlDescricao = "exec sys.sp_updateextendedproperty 'MS_Description','{}','SCHEMA','dbo','TABLE','{}','COLUMN','{}' ".format(
                getattr(objcampo, "funcao"),
                getattr(objcampo, "tabela"),
                getattr(objcampo, "campo"))
            cursor_campo.execute(sqlDescricao)
            cursor_campo.commit()

            sqlDescricao = "UPDATE TB00003 SET TB00003_FUNCAO = '{}' WHERE TB00003_CAMPO = '{}' ".format(
                getattr(objcampo, "funcao"),
                getattr(objcampo, "campo"))
            cursor_campo.execute(sqlDescricao)
            cursor_campo.commit()

            sqlDescricao = "UPDATE TB00101 SET TB00101_FUNCAO = '{}' WHERE TB00101_CAMPO = '{}' ".format(
                getattr(objcampo, "funcao"),
                getattr(objcampo, "campo"))
            cursor_campo.execute(sqlDescricao)
            cursor_campo.commit()

            sqlDescricao = "UPDATE TB00102 SET TB00102_FUNCAO = '{}' WHERE TB00102_CAMPO = '{}' ".format(
                getattr(objcampo, "funcao"),
                getattr(objcampo, "campo"))
            cursor_campo.execute(sqlDescricao)
            cursor_campo.commit()

            cursor_campo.close()
            dados_campo.close()

            return log.geralog(1, "OK", "Campo '{} - {}' alterado com sucesso !".format(getattr(objcampo, "campo"),
                                                                                      getattr(objcampo, "funcao")))
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
    def createView(self, params):
        try:
            # Atibuindo os parâmetros nas variaveis
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])
            objcampo = dao.jsontoObject(df_params.loc["object", 0])
            dados_campos = connect.dataconnect(stoken, 0)
            cursor_campos = dados_campos.cursor()

            cursor_campos.execute(
                "SELECT top 1 COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}' order by ORDINAL_POSITION DESC".format(
                    getattr(objcampo, "view")))
            valores_ultimo = cursor_campos.fetchall()
            descricao_ultimo = cursor_campos.description
            colunas_ultimo = [tp[0] for tp in descricao_ultimo]
            tabela_ultimo = pd.DataFrame.from_records(valores_ultimo, columns=colunas_ultimo)
            sultimocampo = tabela_ultimo["COLUMN_NAME"][0]

            if getattr(objcampo, "view") != getattr(objcampo, "tabela"):
                cursor_campos.execute("sp_helptext {}".format(getattr(objcampo, "view")))
                valores_campos = cursor_campos.fetchall()
                descricao_campos = cursor_campos.description
                colunas_campos = [tp[0] for tp in descricao_campos]
                tabela_campos = pd.DataFrame.from_records(valores_campos, columns=colunas_campos)
                sqlView = ""
                for linha in tabela_campos["Text"]:
                    linha = str(linha).upper().replace("CREATE", "ALTER")
                    if sultimocampo not in linha:
                        sqlView += linha
                    else:
                        if getattr(objcampo, "isforeign") != 1:
                            sqlView += "{},{} ".format(linha, getattr(objcampo, "campo"))+"\n"

                        else:
                            sqlView += "{},{},{} as {}".format(linha, getattr(objcampo, "campo"),
                                                               getattr(objcampo, "tabelaref") + "_" + getattr(objcampo,
                                                                                                              "campo") + "." + getattr(
                                                                   objcampo, "tabelaref") + "_NOME", getattr(objcampo,
                                                                                                             "campo") + "_NOME")+"\n"

                if getattr(objcampo, "isforeign") == 1:
                    sqlView += " LEFT JOIN {} AS {} ON {} = {}.{} ".format(getattr(objcampo, "tabelaref"),
                                                                           getattr(objcampo,
                                                                                   "tabelaref") + "_" + getattr(
                                                                               objcampo, "campo"),
                                                                           getattr(objcampo, "campo"),
                                                                           getattr(objcampo,
                                                                                   "tabelaref") + "_" + getattr(
                                                                               objcampo, "campo"),
                                                                           getattr(objcampo, "tabelaref") + "_CODIGO")

                cursor_campos.execute(sqlView)
                cursor_campos.commit()
            cursor_campos.close()
            dados_campos.close()

            return log.geralog(1, "OK", "View {} modificado com sucesso !".format(getattr(objcampo, "view")))
        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
