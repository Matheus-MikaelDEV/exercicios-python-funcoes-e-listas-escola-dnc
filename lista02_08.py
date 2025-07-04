def quantidadeDeNumerosPares(lista):

    quantidade = 0

    for i in lista:
        if i % 2 == 0:
            quantidade += 1
    return quantidade

print(quantidadeDeNumerosPares([1, 2, 3, 4, 5, 6, 7,8, 9, 10]))