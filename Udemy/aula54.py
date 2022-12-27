import os

lista = []

print('Lista de Compras')

while True:
    opcao = input(
        'Selecione uma opção: \n [i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Nome do produto: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite número inteiro.')
        except IndexError:
            print('Índice não exista na lista.')
        except Exception:
            print('Erro desconhecido.')

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
