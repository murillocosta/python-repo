"""
introdução ao desempacotamento
"""


# nome1, nome2, nome3 = ['Murillo', 'Neco', 'Marina']

# print(nome1)
# print(nome2)
# print(nome3)

nome1, * resto = ['Murillo', 'Neco', 'Marina']
nome1, *_ = ['Murillo', 'Neco', 'Marina']

_, nome2, *_ = ['Murillo', 'Neco', 'Marina']
