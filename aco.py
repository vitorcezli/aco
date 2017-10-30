#!/usr/bin/python3
from leitura_dados import pega_informacoes_pontos
from leitura_dados import pega_distancia_pontos
from leitura_dados import pega_pontos_e_medianas


print(pega_pontos_e_medianas('SJC1.dat'))
informacoes = pega_informacoes_pontos('SJC1.dat')
print(pega_distancia_pontos(informacoes))