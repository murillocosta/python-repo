

print('Calculo de IMC')
nome = input('Digite seu nome: ')
altura = input('Por favor, informe sua aultura(em metros): ')
peso = input('Agora, insira seu peso:')

imc = peso/(altura**2)

print(f'{nome} tem {peso} de altura, pesa {peso}kgs e seu IMC é {imc}')