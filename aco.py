#!/usr/bin/python3
import leitura_dados
import funcoes_artigo


# pega as informações iniciais do arquivo que será utilizado
n_pontos, n_medianas = leitura_dados.pega_pontos_e_medianas('SJC1.dat')
dados = leitura_dados.pega_informacoes_pontos('SJC1.dat')
distancias = leitura_dados.pega_distancia_pontos(dados)

# valores iniciais de feromônios
feromonios = funcoes_artigo.feromonios_iniciais(n_pontos, 0.5)
print(funcoes_artigo.escolhe_pontos_por_valores(feromonios, 10))

# testa o funcionamento da heurística
resultado = funcoes_artigo.constroi_solucao_alocacao(dados, distancias, [0, 10, 20, 21, 22, 23, 24, 25])
print(funcoes_artigo.verifica_consistencia(dados, resultado, [0, 10, 20, 21, 22, 23, 24, 25]))




# teste
print(funcoes_artigo.calcula_distancia_total(distancias, resultado))