# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.


lista = [numero for numero in range(10)]
print(lista)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]


# novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05}
#                   for produto in produtos]

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto}
                  for produto in produtos]

print(*novos_produtos, sep='\n')


lista = [n * 20 for n in range(10) if n < 5]
print('lista', lista)


produtos_filtrados = [
    produto for produto in produtos if produto['preco'] > 20
]

print('Produtos filtrados', produtos_filtrados)
