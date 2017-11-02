import copy
import numpy as np
import random


def __coluna_matriz(matriz, coluna):
	"Retorna a coluna desejada da matriz"
	return [linha[coluna] for linha in matriz]


def __ordena_pontos(distancias, medianas):
	"Ordena os pontos a partir de sua distancia com a mediana mais proxima"
	matriz_distancia = []
	for i in range(len(distancias)):
		# indica o ponto e sua distância à mediana mais próxima
		matriz_distancia.append([i, min([distancias[i][j] for j in medianas])])
	# ordena os pontos de acordo com sua distância à mediana mais próxima
	matriz_distancia = sorted(matriz_distancia, key = lambda x: x[1])
	# retorna os pontos ordenados
	return __coluna_matriz(matriz_distancia, 0)


def __ordena_medianas(ponto, distancias, medianas):
	"Ordena as medianas a partir de sua distancia com o ponto"
	distancia = distancias[ponto]
	matriz_distancia = [[mediana, distancia[mediana]] for mediana in medianas]
	matriz_distancia = sorted(matriz_distancia, key = lambda x: x[1])
	return __coluna_matriz(matriz_distancia, 0)


def constroi_solucao_alocacao(dados, distancias, medianas):
	"Retorna uma solucao para o problema de alocacao"
	# inicializa as variáveis que serão usadas na heurística
	capacidade = copy.deepcopy(dados[:, 2])
	demanda = copy.deepcopy(dados[:, 3])
	n_medianas = len(medianas)
	n_pontos = len(dados)
	x = [[0 for x in range(n_pontos)] for y in range(n_pontos)]

	# executa a heurística do artigo
	pontos = __ordena_pontos(distancias, medianas)
	for indice_ponto in range(n_pontos):
		ponto = pontos[indice_ponto]
		# pontos que são medianas não entram na alocação
		if ponto in medianas:
			continue
		# realiza a alocação a partir das medianas mais próximas
		medianas = __ordena_medianas(ponto, distancias, medianas)
		for indice_mediana in range(n_medianas):
			mediana = medianas[indice_mediana]
			if capacidade[mediana] - demanda[ponto] >= 0:
				x[ponto][mediana] = 1
				capacidade[mediana] -= demanda[ponto]
				break
	# retorna a matriz de alocação
	return np.array(x)


def verifica_consistencia(dados, alocacoes, medianas):
	"Verifica se os dados estao consistentes com as restricoes"
	# algum ponto foi não foi alocado ou utiliza mais de uma mediana
	pontos_usados = np.sum(alocacoes, axis = 1)
	for ponto in range(len(dados)):
		if pontos_usados[ponto] != 1 and ponto not in medianas:
			return False

	# algum ponto que não é uma mediana foi utilizado como tal
	pontos_alocados = np.sum(alocacoes, axis = 0)
	for ponto in range(len(dados)):
		if pontos_alocados[ponto] > 0 and ponto not in medianas:
			return False

	# a demanda em uma mediana não é maior do que sua capacidade
	demanda = dados[:, 3].T
	capacidade = dados[:, 2].T
	demanda_medianas = demanda.dot(alocacoes)
	if (demanda_medianas <= capacidade).any() == False:
		return False
	return True


def calcula_distancia_total(distancias, alocacoes):
	"Calcula a distancia dos pontos as suas medianas"
	return np.sum(distancias * alocacoes)


def feromonios_iniciais(quantidade_pontos, valor_inicial):
	"Retorna a quantidade inicial de feromonios"
	return np.array([valor_inicial for ponto in range(quantidade_pontos)])


def __transforme_valor_probabilidade(valores):
	"Retorna a probabilidade de cada valor"
	return valores / np.sum(valores)


def __seleciona_indice(probabilidades):
	"Seleciona um indice a partir das probabilidades"
	aleatorio = random.random()
	indice = 0
	# calcula o índice e o retorna
	while aleatorio - probabilidades[indice] > 0:
		aleatorio -= probabilidades[indice]
		indice += 1
	return indice


def escolhe_pontos_por_valores(feromonios, quantidade_medianas):
	"Escolhe a quantidade indicada de pontos a partir de seus valores"
	lista_pontos = []
	prob = feromonios

	prob = __transforme_valor_probabilidade(prob)
	lista_indice_prob = list(range(len(feromonios)))

	# seleciona uma mediana a cada iteração a partir dos feromônios
	while len(lista_pontos) < quantidade_medianas:
		indice = __seleciona_indice(prob)
		lista_pontos.append(lista_indice_prob[indice])
		del lista_indice_prob[indice]
		prob = np.delete(prob, indice)
		prob = __transforme_valor_probabilidade(prob)

	# retorna a lista com as medianas selecionadas
	return lista_pontos