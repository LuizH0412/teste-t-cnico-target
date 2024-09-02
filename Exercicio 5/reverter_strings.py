# Função que reverte a string informada utilizando fatiamento
def reverter_string(string):
    string_revertida = string[::-1]
    return string_revertida

palavra = input('Digite qualquer coisa: ')
resultado = reverter_string(palavra)

print(resultado)