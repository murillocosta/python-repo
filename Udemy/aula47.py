palavra_secreta = 'biologia'

palpites_corretos = ''

while True:
    palpite = input('Digite uma letra: ')

    if len(palpite) > 1:
        print('Opa, digite apenas uma letra.')
        continue

    if palpite in palavra_secreta:
        palpites_corretos += palpite

    palavra_correta = ''
    for letra in palavra_secreta:
        if letra in palpites_corretos:
            palavra_correta += letra

        else:
            palavra_correta += '*'

    print(palavra_correta)
