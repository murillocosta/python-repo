primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro_valor_num = float(primeiro_valor)
segundo_valor_num = float(segundo_valor)

if primeiro_valor_num > segundo_valor_num:
  print(f'O {primeiro_valor=} e é maior que o {segundo_valor=}.' )
elif primeiro_valor_num < segundo_valor_num:
  print(f'O {segundo_valor=} e é maior que o {primeiro_valor=}.' )
else:
  print('Os valores são iguais.')