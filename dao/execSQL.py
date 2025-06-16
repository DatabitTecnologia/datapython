import connect
import pandas as pd
import log


class execSQL:

    def execSQL(self, params):
        try:
            # Atibuindo os parâmetros nas variaveis
            df_params = pd.DataFrame.from_dict(params, orient="index")
            stoken = str(df_params.loc["token", 0])
            ssql = df_params.loc["sql", 0]
            cursor = df_params.loc["cursor", 0]
            # Criando conexão com o Banco de Dados
            dados_execute = connect.dataconnect(stoken, 0)
            cursor_procedure = dados_execute.cursor()

            cursor_procedure.execute(ssql)
            if not "SELECT" in ssql.upper():
                try:
                    if cursor == "N":
                        cursor_procedure.commit()
                        cursor_procedure.close()
                        dados_execute.close()
                except Exception as erro:
                    print(erro)

            if cursor == "S":
               valores_lista = cursor_procedure.fetchall()
               descricao_lista = cursor_procedure.description
               colunas_lista = [tp[0] for tp in descricao_lista]
               tabela_lista = pd.DataFrame.from_records(valores_lista, columns=colunas_lista)
               tabela_lista.head()
               sJson = tabela_lista.to_json(orient="records")
               cursor_procedure.commit()
               cursor_procedure.close()
               dados_execute.close()
               return sJson
            else:
                return log.geralog(1, "OK", "Operacao executada com Sucesso !")



        except Exception as erro:
            return log.geralog(-1, "ERRO", f"{erro=}")
