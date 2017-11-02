#!/usr/bin/python3
import math
import numpy as np


def pega_pontos_e_medianas(file):
	"Retorna uma lista com o numero de pontos e de medianas"
	file = open(file).read().split()
	return [int(file[i]) for i in range(2)]


def pega_informacoes_pontos(file):
	"Retorna uma matriz com as informacoes de cada ponto"
	# cria uma matriz com as linhas do arquivo
	matriz = []
	file = open(file).read().split('\n')
	for linha in file[1 :]:
		matriz.append([int(coluna) for coluna in linha.split()])

	# remove a última linha se ela for vazia e retorna a matriz
	if len(matriz[len(matriz) - 1]) != 4:
		matriz = matriz[: len(matriz) - 1]
	return np.array(matriz)


def pega_distancia_pontos(matriz):
	"Retorna a distancia entre cada par de pontos da matriz"
	# inicializa a matriz de distância
	distancia = [[0 for i in range(len(matriz))] 
		for j in range(len(matriz))]

	# calcula a distância entre cada par e retorna a matriz
	for i in range(len(distancia)):
		for j in range(len(distancia[0])):
			distancia[i][j] = math.sqrt(
				(matriz[i][0] - matriz[j][0]) ** 2 +
				(matriz[i][1] - matriz[j][1]) ** 2
			)
	return np.array(distancia)