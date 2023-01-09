pessoa = {
    'nome': 'Murillo',
    'sobrenome': 'Costa',
    'altura': 1.83,
    'estilos_musicais': ['mpb', 'reggae', 'rock']
}

print(pessoa['nome'])
print(pessoa['sobrenome'])


for chave in pessoa:
    print(chave, pessoa[chave])
