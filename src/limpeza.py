import re

def limpar_texto(texto):
    texto = texto.lower()

    #remover links
    texto = re.sub(r"httl\S+", "", texto)

    #remove usuários @
    texto = re.sub(r"@\w+", "", texto)

    #remove caract especial
    texto = re.sub(r"[^a-zA-Z\s]", "", texto)

    return texto