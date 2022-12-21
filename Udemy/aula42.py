frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.'

frase_lower = frase.lower()

i = 0
mais_vezes = 0
letra_mais_vezes = ''


while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    vezes_letra = frase.count(letra_atual)

    if mais_vezes < vezes_letra:
        mais_vezes = vezes_letra
        letra_mais_vezes = letra_atual

    i += 1

print(
    f'A letra que mais apareceu foi "{letra_mais_vezes}", que apareceu {mais_vezes} vezes.')
