###### CALCULADORA COM WHILE ######

firula = '~*' * 10
print(firula, 'Bem-Vindo à Calculadora', firula)

while True:
    resultado = 0
    num_1 = input('Digite o primeiro número: ').strip()
    num_2 = input('Digite o segundo número: ').strip()
    numeros_validos = None

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos números são inválidos.')
        continue

    operador = input('Digite o operador: \n \
      Somar ( + )\n \
      Subtrair ( - )\n \
      Multiplicar ( * )\n \
      Divdir ( / ): ').strip()

    OPERADORES_PERMITIDOS = '+ - * /'

    if operador not in OPERADORES_PERMITIDOS:
        print(
            'O Operador digitado não é válido. [Operadores válidos: + - * / ]')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        resultado = num_1_float + num_2_float
    elif operador == '-':
        resultado = num_1_float - num_2_float
    elif operador == '*':
        resultado = num_1_float * num_2_float
    elif operador == '/':
        resultado = num_1_float / num_2_float

    print('Resultado: ', resultado)

    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    if sair:
        print('Encerrando calculadora...')
        break
    print(firula, 'Reiniciando Calculadora...', firula)
