

print('~*' * 5,'Calculo de IMC', '*~' * 5 )
nome = input('Digite seu nome: ')
altura = float(input('Por favor, informe sua altura(em metros): '))
peso = float(input('Agora, insira seu peso: '))

imc = peso/(altura**2)

print('~*' * 15)

print(f'{nome} tem {altura} de altura, pesa {peso}kgs e seu IMC é {imc:.2f}.')