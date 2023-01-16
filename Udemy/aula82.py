def executa(funcao, *args):
    return funcao(*args)


# def soma(x,y):
#   return x + y

lambda x, y: x + y

print(executa(
    lambda x, y: x + y, 10, 5
))


duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(5))
