
firula = '~*~' * 5

print(f'{firula}Exercício{firula}')
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nom é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    if ' ' in nome:
        print(f'Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpa, você deixou campos vazios.')
