# numero_digitado = input('Digite um número: ')

# if numero_digitado.isdigit():
#     numero_int = int(numero_digitado)
#     if numero_int % 2 == 0:
#         print(f'O número {numero_digitado} é par.')
#     elif numero_int % 2 != 0:
#         print(f'O número {numero_digitado} é ímpar.')
#     else:
#         print('Zero é neutro xD')
# else:
#     print('Você não digitou um número inteiro.')


# hora_digitada = input('Digite a hora atual(apenas as horas): ')
# hora = int(hora_digitada)

# if (hora <= 23 and hora >= 18):
#     print('Boa noite!')
# elif (hora <= 17 and hora >=12):
#     print('Boa tarde!')
# else:
#     print('Bom dia!')

nome_digitado = input('Por favor, digite seu nome: ')

if nome_digitado:
    
    tamanho_nome_digitado = len(nome_digitado)

    if tamanho_nome_digitado <= 4:
        print('Seu nome é curto')
    elif tamanho_nome_digitado > 4 and tamanho_nome_digitado <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Você não digitou nada!')