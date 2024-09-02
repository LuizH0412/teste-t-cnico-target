import json

# Função que carrega os dados do arquivo JSON e retorna eles para a variável
def carregar_dados():
    with open('./faturamento.json', 'r') as arquivo:
        return json.load(arquivo)
    
# Função que calcula o faturamento da distribuidora seguindo os critérios estabelecidos
def calcular_faturamento(dados):
    faturamentos = []

    for item in dados['faturamento_diario']:
        if item['faturamento'] > 0:
            faturamentos.append(item['faturamento'])
    
    if not faturamentos:
        return {
            "menor_valor": None,
            "maior_valor": None,
            "dias_acima_da_media": 0
        }

    maior_valor = max(faturamentos)
    menor_valor = min(faturamentos)

    media_do_mes = sum(faturamentos) / len(faturamentos)

    dias_acima_da_media = 0

    for item in dados['faturamento_diario']:
        if item['faturamento'] > media_do_mes:
            dias_acima_da_media += 1
        
    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_da_media": dias_acima_da_media
    }


dados = carregar_dados()

calculo = calcular_faturamento(dados)

print(f'Maior valor de faturamento: R${calculo['maior_valor']:.2f}')
print(f'Menor valor de faturamento: R${calculo['menor_valor']:.2f}')
print(f'Número de dias com faturamento acima da média: {calculo['dias_acima_da_media']}')