"""
File : codigo.py

Function : Métodos para tratamento de código sequencial

Author: Sidney Sanches Moreira
"""


def addcodigo(scodigo):
    """
    Método de criação de código incremental alfanumérico
    :param scodigo: Código anterior
    :return: str -> Novo Código
    """
    scodigo = scodigo.upper()
    itamanho = len(scodigo)
    sletra2 = [None] * itamanho
    snovocodigo = scodigo
    icont = itamanho
    while icont > 0:
        sletra = scodigo[icont - 1: icont]
        for icont2 in range(icont):
            sletra2[icont2 - 1] = scodigo[icont2 - 1: icont2]
        if sletra in "012345678":
            snovocodigo = snovocodigo[0:icont - 1] + str(int(sletra) + 1) + snovocodigo[icont:itamanho]
            break
        if sletra == "9":
            bpossui9 = True
            for icont2 in range(icont):
                if sletra2[icont2] != "9":
                    bpossui9 = False
                    break

            if bpossui9:
                print(1)
                snovocodigo = snovocodigo[0:icont - 1] + "A" + snovocodigo[icont:itamanho]
                break
            else:
                print(2)
                snovocodigo = snovocodigo[0:icont - 1] + "0" + snovocodigo[icont:itamanho]

        if sletra not in "0123456789":
            if sletra != "Z":
                snovocodigo = snovocodigo[0:icont - 1] + chr(ord(sletra[0]) + 1) + snovocodigo[icont:itamanho]
                break
            else:
                snovocodigo = snovocodigo[0:icont - 1] + "0" + snovocodigo[icont:itamanho]

        icont -= 1

    return snovocodigo
#if __name__ == "__main__":
#    print(addcodigo("999"))