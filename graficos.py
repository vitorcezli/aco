#!/usr/bin/python3
import matplotlib.pyplot as plt


def plota_distancia(distancias):
	"Plota um grafico em que x e a interacao e y a distancia total"
	plt.plot(range(1, len(distancias) + 1), distancias, '.')
	plt.show()


def plota_resultado(resultados):
	"Plota uma curva gaussiana com os resultados obtidos"
	media = np.mean(resultados)
	variancia = np.var(resultados)
	desvio = math.sqrt(variancia)
	x = np.linspace(media - 3 * desvio, media + 3 * desvio, 100)
	plt.plot(x, mlab.normpdf(x, media, desvio))
	plt.show()