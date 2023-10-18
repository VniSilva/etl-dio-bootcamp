import pandas as pd

# LOAD

'''
    Carregando arquivo .csv com as colunas id, nome, email e ocupacao
'''

dados = pd.read_csv('dados.csv')

# TRANSFORM 

'''
    Alterando aspectos da estrutura com os dados já estruturados em um DataFrame
'''

dados.rename(str.upper, axis='columns', inplace=True)
dados.set_index('ID', inplace=True)

# EXTRACT

'''
    Passando os dados para um novo formato de arquivo
'''

dados.to_json('dados.json')
