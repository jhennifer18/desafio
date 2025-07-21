def intercalar_listas(lista1, lista2):
    intercalada = []
    for i in range(len(lista1)):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])
    return intercalada
