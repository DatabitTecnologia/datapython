"""
File : crypto.py

Function: Metodos para recursos de criptografia

Author: Sidney Sanches Moreira
"""


def dbencrypt(svalor):
    """
    Metodo pra criptografiar informacoes

    :param svalor: Valor que precisa ser criptografado

    :return: str -> Valor Criptografado
    """
    if svalor != "":
        key = "WQKLEWUQMNDSJKEHJKSADFHUWNDJHXCJKHFRJKUIHSADNSCHBGBGFKJAWSDNUSA"

        keylen = len(key)
        keypos = -1
        scrpos = 0
        offset = 24
        dest = "{0:X}".format(offset)

        while scrpos <= len(svalor) - 1:
            scrasc = (ord(svalor[scrpos]) + offset) % 255
            if keypos < keylen:
                keypos += 1
            else:
                keypos = 0
            scrasc = scrasc ^ ord(key[keypos])
            termo = "{0:X}".format(scrasc)
            tamanho = len(termo)
            if tamanho > 1:
                dest = dest + termo
            else:
                dest = dest + "0" + termo
            offset = scrasc
            scrpos += 1

    return dest


def dbdecrypt(svalor):
    """
    Metodo pra descriptografiar informacoes

    :param svalor: Valor criptografado

    :return: str -> Valor descriptografado

    """
    if svalor != "":
        key = "WQKLEWUQMNDSJKEHJKSADFHUWNDJHXCJKHFRJKUIHSADNSCHBGBGFKJAWSDNUSA"
        keylen = len(key)
        keypos = -1
        scrpos = 2
        offset = int(svalor[0:2], 16)

        dest = ""
        while True:
            srcasc = int(svalor[scrpos:scrpos + 2], 16)
            if keypos < keylen:
                keypos += 1
            else:
                keypos = 0
            tmpsrcasc = srcasc ^ ord(key[keypos])
            if tmpsrcasc <= offset:
                tmpsrcasc = 255 + tmpsrcasc - offset
            else:
                tmpsrcasc = tmpsrcasc - offset
            dest = dest + chr(tmpsrcasc)
            offset = srcasc
            scrpos = scrpos + 2
            if len(svalor) <= scrpos:
                break

    return dest


#if __name__ == "__main__":
#    print(dbencrypt("DATACLASSIC"))
#    print(dbdecrypt("180B1D3A373FDC4BCF6EF979"))
