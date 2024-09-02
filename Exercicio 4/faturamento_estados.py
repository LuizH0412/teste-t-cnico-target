import json

# Função que carrega dos dados no arquivo JSON
def carregar_dados():
    with open('./Exercicio 4/faturamento_estados.json', 'r') as arquivo:
        return json.load(arquivo)
    
# Função que calcula o percentual de representação de cada estado individualmente e retorna para uma variável
def calcular_percentual(dados):
    total_faturamento = 0

    for item in dados['faturamento']:
        total_faturamento += item['valor']

    
    percentuais = []
    for item in dados['faturamento']:
        estado = item['estado']
        valor = item['valor']
        perceltual = (valor / total_faturamento) * 100
        percentuais.append({
            'estado': estado,
            'percentual': round(perceltual, 2)
        })
    
    return percentuais


dados = carregar_dados()
percentuais = calcular_percentual(dados)

# Retorna no console o percentual de representação de cada estado
for percentual in percentuais:
    print(f'Estado: {percentual['estado']}, Percentual de Represetação: {percentual['percentual']}%')