def maiorNumeroDaLista(lista):

    for i in range(len(lista)):
        if i == 0:
            maior = lista[i]
        elif lista[i] > maior:
            maior = lista[i]
    return maior

print(maiorNumeroDaLista([34, 4, 56, 23, 12]))