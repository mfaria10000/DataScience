#functiona to return the average of the items in the list
def calc_media(lista):
    tamanho = len(lista)
    total = sum(lista)
    media = total / tamanho
    return media