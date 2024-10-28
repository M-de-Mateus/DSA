# -*- coding: utf-8 -*-
"""
Criado por: Mateus Nunes (com auxilio do chat GPT4º)
LinkedIn: https://www.linkedin.com/in/mateussantosnunes/
"""
#%%
!pip install scipy
!pip install tabulate
!pip install matplotlib
#%%

# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
from scipy import stats
from tabulate import tabulate
import matplotlib.pyplot as plt

# o comando 'from scipy import stats' está importando apenas a função stats
# da biblioteca scipy
# Lendo o arquivo que contém os dados a serem analizados (DataFrame)

df = pd.read_excel('Exercicio 2.xlsx',
                   dtype={'Meses': str, 'Ação 1': float, 'Ação 2': float})

# Contando o número de observações de colunas distintas (apenas para seguir o exercicio)

obs_acao1 = df[df.columns[1]].count()
obs_acao2 = df[df.columns[2]].count()

# calculando média das colunas (maneira alternativa de selecionar uma coluna)
# também é possivel ler uma coluna usando "df.coluna_desejada", porém como há
# um espaço no nome "Ação 1" esse metodo não funciona

media_acao1 = df['Ação 1'].mean()
media_acao2 = df['Ação 2'].mean()

# calculando a mediana das colunas

mediana_acao1 = df['Ação 1'].median()
mediana_acao2 = df['Ação 2'].median()

# calculando os quartis
# é possivel calcular os quartis de uma maneira mais rápida
# basta selecionar uma coluna e passar os quartis como argumentos para a função
# Ex.: q1_acao1 = df['Ação 1'].quantile([0.25, 0.5, 0.75])
# Isso irá criar uma 'tabela' com o Q1, a mediadna e o Q3

# Primeiro quartil
q1_acao1 = df['Ação 1'].quantile(0.25)
q1_acao2 = df['Ação 2'].quantile(0.25)

# Terceiro quartil
q3_acao1 = df['Ação 1'].quantile(0.75)
q3_acao2 = df['Ação 2'].quantile(0.75)

# calculando os decis
# A função quantile também calcula os decis, basta ajustarmos a porcentagem
# passada no argumento

# 8º decil

oito_decil_acao1 = df['Ação 1'].quantile(0.8)
oito_decil_acao2 = df['Ação 2'].quantile(0.8)

# 9º decil

nono_decil_acao1 = df['Ação 1'].quantile(0.9)
nono_decil_acao2 = df['Ação 2'].quantile(0.9)

# calculando os percentis
# A função quantile também calcula os percentis, basta ajustarmos a porcentagem
# passada no argumento

# 27º percentil

vigsetimo_percentil_acao1 = df['Ação 1'].quantile(0.27)
vigsetimo_percentil_acao2 = df['Ação 2'].quantile(0.27)

# 64º percentil

sexquarto_percentil_acao1 = df['Ação 1'].quantile(0.64)
sexquarto_percentil_acao2 = df['Ação 2'].quantile(0.64)

# Calculando o valor minimo

min_acao1 = df['Ação 1'].min()
min_acao2 = df['Ação 2'].min()

# Calculando o valor máximo

max_acao1 = df['Ação 1'].max()
max_acao2 = df['Ação 2'].max()

# Caculando a amplitude
# Como já temos o valor minimo e o máximo armazenados em variáveis
# Podemos usa-las para simplicar o metodo de calculo
# Ex de calculo sem as variáveis: 
# amplitude_acao1 =  df['Ação 1'].max() -  df['Ação 1'].min()

amplitude_acao1 =  max_acao1 - min_acao1
amplitude_acao2 =  max_acao2 - min_acao2

# Calculando a variancia

var_acao1 = df['Ação 1'].var()
var_acao2 = df['Ação 2'].var()

# Calculando o desvio padrão

dpadrao_acao1 = df['Ação 1'].std()
dpadrao_acao2 = df['Ação 2'].std()

# Calculando o erro padrão
# Como já temos o valor minimo e o máximo armazenados em variáveis
# Podemos usa-las para simplicar o metodo de calculo
# Ex de calculo sem as variáveis: 
# df['Ação 2'].std() / (df[df.columns[2]].count() ** 0.5)
# numero ** 0.5 = raiz quadrada

erropadrao_acao1 = df['Ação 1'].std() / (obs_acao1 ** 0.5)
erropadrao_acao2 = df['Ação 2'].std() / (obs_acao2 ** 0.5)

# Calculando Coeficiente de variação

coefvar_acao1 = dpadrao_acao1 / media_acao1
coefvar_acao2 = dpadrao_acao2 / media_acao2

# Calculando a correlação

correlacao = df['Ação 1'].corr(df['Ação 2'])

# Estatistica T de correlação

estatistica_t = correlacao * ((obs_acao1 - 2 ) ** 0.5) / ((1 - correlacao ** 2) ** 0.5)

# p-valor
# A função abs() remove um possivel sinal negativo de T
# Ex.: abs(-2) = 2

# p-valor para teste bicaudal

p_valor = stats.t.sf(abs(estatistica_t), df = obs_acao1 - 2) * 2

# Valor critico
# alpha = 0.05

valor_critico = stats.t.ppf(1 - 0.05 / 2, obs_acao1 - 2)

descritivas_dados = {
    'Métrica': ['Nº Obs', 'Média', 'Mediana', '1º Quartil', '3º Quartil', '8º Decil',
                '9º Decil', '27º Percentil', '64º Percentil', 'Valor Mínimo', 'Valor Máximo',
                'Amplitude', 'Variância', 'Desvio Padrão', 'Erro Padrão', 'Coeficiente de Variação'],
    'Ação 1': [obs_acao1, media_acao1, mediana_acao1, q1_acao1, q3_acao1, oito_decil_acao1, nono_decil_acao1, vigsetimo_percentil_acao1,
               sexquarto_percentil_acao1, min_acao1, max_acao1, amplitude_acao1, var_acao1, dpadrao_acao1,
               erropadrao_acao1, coefvar_acao1],
    'Ação 2': [obs_acao2, media_acao2, mediana_acao2, q1_acao2, q3_acao2, oito_decil_acao2, nono_decil_acao2, vigsetimo_percentil_acao2,
               sexquarto_percentil_acao2, min_acao2, max_acao2, amplitude_acao2, var_acao2, dpadrao_acao2,
               erropadrao_acao2, coefvar_acao2]
    }

resultados_dados = {
    'Métrica': ['Correlação', 'Estatística T', 'P-valor (bicaudal)', 'Valor Crítico (5%)'],
    'Resultado': [correlacao, estatistica_t, p_valor, valor_critico]
    }

estatisticas_descritivas = pd.DataFrame(descritivas_dados)
resultados = pd.DataFrame(resultados_dados)

print(tabulate(estatisticas_descritivas, headers='keys', tablefmt='grid'))
print(tabulate(resultados, headers='keys', tablefmt='grid'))

#%%

# Passando tudo para uma única função
# Uma função pode agrupar diversos processos dentro dela
# def é usado para iniciar a função
# logo depois vem o nome que você mesmo atribui a função
# por ultimos os argumentos da função, que são as variáveis com as quais ela irá trabalhar
# o alpha é um argumento opcional e o seu valor padrão é 0.05 do tipo float
# defini o nome das colunas como string para facilitar no caso de nomes de colunas com espaço


def estatisticas_descritivas_func(data_frame, nome_col1: str, nome_col2: str, alpha: float = 0.05,
                                  to_excel = False, show_plot = False):
    obs = data_frame.shape[0]
    
    media1= data_frame[nome_col1].mean()
    media2 = data_frame[nome_col2].mean()
    
    mediana1 = data_frame[nome_col1].median()
    mediana2 = data_frame[nome_col2].median()
    
    q11 = data_frame[nome_col1].quantile(0.25)
    q12 = data_frame[nome_col2].quantile(0.25)
    
    q31 = data_frame[nome_col1].quantile(0.75)
    q32 = data_frame[nome_col2].quantile(0.75)
    
    oito_decil1 = data_frame[nome_col1].quantile(0.8)
    oito_decil2 = data_frame[nome_col2].quantile(0.8)
    
    nono_decil1 = data_frame[nome_col1].quantile(0.9)
    nono_decil2 = data_frame[nome_col2].quantile(0.9)
    
    vigsetimo_percentil1 = data_frame[nome_col1].quantile(0.27)
    vigsetimo_percentil2 = data_frame[nome_col2].quantile(0.27)
    
    sexquarto_percentil1 = data_frame[nome_col1].quantile(0.64)
    sexquarto_percentil2 = data_frame[nome_col2].quantile(0.64)
    
    min1 = data_frame[nome_col1].min()
    min2 = data_frame[nome_col2].min()
    
    max1 = data_frame[nome_col1].max()
    max2 = data_frame[nome_col2].max()
    
    amplitude1 =  max1 - min1
    amplitude2 =  max2 - min2
    
    var1 = data_frame[nome_col1].var()
    var2 = data_frame[nome_col2].var()
    
    dpadrao1 = data_frame[nome_col1].std()
    dpadrao2 = data_frame[nome_col2].std()
    
    erropadrao1 = data_frame[nome_col1].std() / (obs ** 0.5)
    erropadrao2 = data_frame[nome_col2].std() / (obs ** 0.5)
    
    coefvar1 = dpadrao1 / media1
    coefvar2 = dpadrao2 / media2
    
    correlacao = data_frame[nome_col1].corr(data_frame[nome_col2])
    
    estatistica_t = correlacao * ((obs - 2 ) ** 0.5) / ((1 - correlacao ** 2) ** 0.5)
    
    p_valor = stats.t.sf(abs(estatistica_t), df = obs - 2) * 2
    
    valor_critico = stats.t.ppf(1 - alpha / 2, obs - 2)
    
    descritivas_dados = {
        'Métrica': ['Nº Obs', 'Média', 'Mediana', '1º Quartil', '3º Quartil', '8º Decil',
                    '9º Decil', '27º Percentil', '64º Percentil', 'Valor Mínimo', 'Valor Máximo',
                    'Amplitude', 'Variância', 'Desvio Padrão', 'Erro Padrão', 'Coeficiente de Variação'],
        'Ação 1': [obs, media1, mediana1, q11, q31, oito_decil1, nono_decil1, vigsetimo_percentil1,
                   sexquarto_percentil1, min1, max1, amplitude1, var1, dpadrao1,
                   erropadrao1, coefvar1],
        'Ação 2': [obs, media2, mediana2, q12, q32, oito_decil2, nono_decil2, vigsetimo_percentil2,
                   sexquarto_percentil2, min2, max2, amplitude2, var2, dpadrao2,
                   erropadrao2, coefvar2]
        }

    resultados_dados = {
        'Métrica': ['Correlação', 'Estatística T', 'P-valor (bicaudal)', 'Valor Crítico (5%)'],
        'Resultado': [correlacao, estatistica_t, p_valor, valor_critico]
        }
    
    estatisticas_descritivas = pd.DataFrame(descritivas_dados)
    resultados = pd.DataFrame(resultados_dados)
      
    if to_excel:
        with pd.ExcelWriter("estatistica_descritiva.xlsx") as writer:
            estatisticas_descritivas.to_excel(writer, sheet_name='Descritivas',
                                              index = False)
            resultados.to_excel(writer, sheet_name='Resultados', index = False)
        return 'Arquivo salvo com sucesso!'
    
    if show_plot:
        # Distribuição t-Student para o gráfico bicaudal
        x = np.linspace(-4, 4, 1000)
        y = stats.t.pdf(x, df=obs - 2)
        
        # Criando o gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', label=f'Distribuição t (df={obs - 2})')
        
        # Região de rejeição (cauda esquerda e direita)
        x_rejeicao_esquerda = np.linspace(-4, -valor_critico, 100)
        y_rejeicao_esquerda = stats.t.pdf(x_rejeicao_esquerda, df=obs - 2)
        plt.fill_between(x_rejeicao_esquerda, y_rejeicao_esquerda, color='red', alpha=0.3)
        
        x_rejeicao_direita = np.linspace(valor_critico, 4, 100)
        y_rejeicao_direita = stats.t.pdf(x_rejeicao_direita, df=obs - 2)
        plt.fill_between(x_rejeicao_direita, y_rejeicao_direita, color='red', alpha=0.3, label=f'Região de Rejeição (α={alpha})')
        
        # Linhas verticais para o valor crítico e a estatística t
        plt.axvline(-valor_critico, color='red', linestyle='--', label=f'Valor Crítico: ±{valor_critico:.2f}')
        plt.axvline(valor_critico, color='red', linestyle='--')
        plt.axvline(estatistica_t, color='green', linestyle='--', label=f'Estatística T: {estatistica_t:.4f}')
        
        # Título e legendas
        plt.title('Distribuição t-Student com Região de Rejeição Bicaudal')
        plt.xlabel('Valores t')
        plt.ylabel('Densidade de Probabilidade')
        plt.legend()
        plt.show()
        
    return estatisticas_descritivas, resultados
            
#%%

#printa as duas variaveis retornadasa
estatisticas_descritivas_func(df, 'Ação 1', 'Ação 2')
#printa somente as estatisticas descritivas
estatisticas_descritivas_func(df, 'Ação 1', 'Ação 2')[0]
#printa somente os resultados
estatisticas_descritivas_func(df, 'Ação 1', 'Ação 2')[1]

#Armazena as duas variaveis retornadas em variaveis distintas
estatis, results = estatisticas_descritivas_func(df, 'Ação 1', 'Ação 2')

#exporta os resultados para excel
estatisticas_descritivas_func(df, 'Ação 1', 'Ação 2', to_excel= True)

#plotando um gráfico
estatisticas_descritivas_func(df, 'Ação 1', 'Ação 2', show_plot= True)

#%%






