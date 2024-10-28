# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:02:20 2024

@author: Mateus
"""
#%%
from scipy.stats import binom
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# a) Ter vitória em 4 jogadas.
# b) Ter vitória em pelo menos 7 jogadas.

def dist_binomial(prob_sucesso, num_repeticoes, sucessos, cumulativa = 6):
    
    if cumulativa == 0:
        prob_exata = binom.pmf(sucessos, num_repeticoes, prob_sucesso)
        return(f'A probabilidade de extatamente {sucessos} sucessos em {num_repeticoes} é de: {prob_exata:.6f}')
    else:
        prob_acumulada = binom.cdf(sucessos, num_repeticoes, prob_sucesso) - binom.cdf( cumulativa , num_repeticoes, prob_sucesso)
        return(f'A probabilidade de sucessos em até {cumulativa + 1} jogadas é de: {prob_acumulada:.6f}')

dist_binomial(0.1667, 10, 10)

#%%

# Chances de sucesso em n repetições
def dist_binomial_2(num_repeticoes_n: int, prob_sucessos_p, sucessos_k, cumulativa = False, dist = False):
    if cumulativa == False and dist == False:
        prob_exata = binom.pmf(sucessos_k, num_repeticoes_n, prob_sucessos_p)
        return(f'A probabilidade de sucessos em {sucessos_k} repetições é de: {prob_exata:.4f}')
    elif cumulativa and dist == False:
        prob_acumulada = binom.cdf(sucessos_k, num_repeticoes_n, prob_sucessos_p)
        return(f'A probabilidade de sucessos acumulada em {sucessos_k} repetições é de: {prob_acumulada:.4f}')
    else:
        dist = [binom.pmf(k, num_repeticoes_n, prob_sucessos_p) for k in range(0, sucessos_k + 1)]
        prob_dist = pd.Series(dist)
        
        plt.figure(figsize=(8, 4))
        plt.plot(prob_dist.index[:13], prob_dist.values[:13], 'o', color='blue')
        plt.title("Distribuição Binomial")
        plt.xlabel("Número de Sucessos")
        plt.ylabel("Probabilidade")
        plt.grid(True)
        plt.show()
        
        prob_dist = prob_dist.apply(lambda x: f'{x:.2f}')
        return prob_dist[:13]
    
dist_binomial_2(65, 0.0650, 6, cumulativa = True)
#%%