"""
File : cnpj.py

Function : Metodo de consulta CNPJ na receita

Author: Sidney Sanches Moreira
"""
import requests
import log


def consultaCNPJ(cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'

    try:
        response = requests.get(url)

        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return log.geralog(-1, 'ERRO', {response.status_code} - {response.text})

    except requests.exceptions.RequestException as e:
        return log.geralog(-1, 'ERRO', e)


#if __name__ == "__main__":
#    print(consultaCNPJ('00650512000101'))
