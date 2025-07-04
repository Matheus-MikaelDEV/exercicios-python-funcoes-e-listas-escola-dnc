def par (num):

    if num % 2 == 0:
        return True
    else:
        return False

def impar (num):
    if num % 2 != 0:
        return True
    else:
        return False

print(par(10))
print(impar(11))