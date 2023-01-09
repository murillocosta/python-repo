def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado_multiplicacao = multiplica(2, 3, 4, 28)

print(resultado_multiplicacao)


def par_impar(numero):
    return f'{numero} é Par.' if numero % 2 == 0 else f'{numero} é Ímpar.'


print(par_impar(3))
