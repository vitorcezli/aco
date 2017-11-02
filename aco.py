#!/usr/bin/python3
import leitura_dados
import funcoes_artigo
import math
import sys


# pega os valores dos parâmetros
quantidade_iteracoes = int(sys.argv[2])
quantidade_formigas = int(sys.argv[3])
taxa = float(sys.argv[4])

# pega as informações iniciais do arquivo que será utilizado
n_pontos, n_medianas = leitura_dados.pega_pontos_e_medianas(sys.argv[1])
dados = leitura_dados.pega_informacoes_pontos(sys.argv[1])
distancias = leitura_dados.pega_distancia_pontos(dados)

# valores iniciais de feromônios
feromonios = funcoes_artigo.feromonios_iniciais(n_pontos, 0.5)

# armazena as melhores medianas
melhores_medianas = None
menor_distancia = math.inf

# executa aco
for iteracao in range(quantidade_iteracoes):
	# armazena as melhores medianas locais
	melhores_medianas_locais = None
	menor_distancia_local = math.inf
	# armazena os piores valores locais
	pior_distancia_local = -math.inf
	# executa para cada formiga
	for formiga in range(quantidade_formigas):
		# seleciona novas medianas e realiza novas alocações
		medianas = funcoes_artigo.escolhe_pontos_por_valores(feromonios, n_medianas)
		alocacoes = funcoes_artigo.constroi_solucao_alocacao(dados, distancias, medianas)
		# verifica se as novas alocações são permitidas
		consistente = funcoes_artigo.verifica_consistencia(dados, alocacoes, medianas)
		if not consistente:
			continue
		# pega a distância dessa iteração
		distancia = funcoes_artigo.calcula_distancia_total(distancias, alocacoes)
		# armazena o novo resultado caso ele seja melhor do que o local
		if distancia < menor_distancia_local:
			menor_distancia_local = distancia
			melhores_medianas_locais = medianas
		# armazena o novo resultado caso ele seja melhor do que o global
		if distancia < menor_distancia:
			menor_distancia = distancia
			melhores_medianas = medianas
		if distancia > pior_distancia_local:
			pior_distancia_local = distancia
	# atualiza feromônios
	funcoes_artigo.atualiza_feromonios(feromonios, taxa,
		melhores_medianas_locais, melhores_medianas,
		menor_distancia_local, menor_distancia, pior_distancia_local)
	print(iteracao + 1, menor_distancia, feromonios)


# imprime a melhor distância e as melhores medianas encontradas
print('Distancia:', menor_distancia)
print('Medianas:', melhores_medianas)