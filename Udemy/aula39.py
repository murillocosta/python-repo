'''
Iterando string com while
'''

nome = 'Murillo Costa'  # iteráveis

tamanho_nome = len(nome)

nova_str = ''
indice = 0


while indice < tamanho_nome:
    for letra in nome:
        nova_str += f'*{letra}'
        indice += 1

print(nova_str)
