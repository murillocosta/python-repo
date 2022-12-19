# operadores in e not in

letra = 'y'
# letra = 'a'

if letra in 'abcdf':
    print('tem')
else:
    print('não tem')


arr = ['a', 'b', 'c']

if letra in arr:
    print('tem na array')
else: 
    print('não tem na array') 

(letra in arr and print('funciona')) or (not letra in arr and print('funciona mas não tem.'))