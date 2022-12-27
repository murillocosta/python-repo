# CPF = '74682489070'
cpf_enviado = '24594059015'

cpf = cpf_enviado.replace('.', '').replace(' ', '').replace('-', '')

cpf_9_iniciais = cpf[:9]

# cpf_9_iniciais_mais_primeiro = cpf_9_iniciais + CPF[0]
cpf_9_iniciais_mais_primeiro = cpf_9_iniciais + '1'


soma_numeros_cpf = 0
multiplicador = 11


for numero in cpf_9_iniciais_mais_primeiro:
    soma_numeros_cpf += int(numero) * multiplicador
    multiplicador -= 1

numero_gerado = (soma_numeros_cpf * 10) % 11

digito2 = 0 if numero_gerado > 9 else numero_gerado

print(digito2)
