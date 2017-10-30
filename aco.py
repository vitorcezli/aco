#!/usr/bin/python3
from leitura_dados import pega_informacoes_pontos
from leitura_dados import pega_distancia_pontos
from leitura_dados import pega_pontos_e_medianas
from funcoes_artigo import constroi_solucao_alocacao
import copy
import numpy as np


# pega as informações iniciais do arquivo que será utilizado
n_pontos, n_medianas = pega_pontos_e_medianas('SJC1.dat')
dados = np.array(pega_informacoes_pontos('SJC1.dat'))
distancias = np.array(pega_distancia_pontos(dados))

# valores iniciais de feromônios
feromonios = np.array([0 for ponto in range(n_pontos)])

resultado = np.asmatrix(constroi_solucao_alocacao(dados, distancias, [0, 10, 22, 34, 45, 78, 45, 12, 77]))

for linha in resultado:
	print(linha)