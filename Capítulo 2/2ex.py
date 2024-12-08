import random
import math
import numpy as np
from matplotlib import pyplot as plt

def pi_montecarlo(N, plot=False, verbose=True):
    if plot:
        fig, ax = plt.subplots()
        fig.set_size_inches(4, 4)
        circle = plt.Circle((0, 0), 1, color='lightblue')
        square = plt.Rectangle((-1, -1), 2, 2, color='red', alpha=0.7)
        ax.add_patch(square)
        ax.add_patch(circle)

    
    N_in = 0  # Pontos dentro do círculo
    cont = 0

    
    while cont < N:  # Quantidade de iterações
        x = random.uniform(-1, 1)  # Valor do eixo X
        y = random.uniform(-1, 1)  # Valor do eixo Y
        z = x**2 + y**2  # Fórmula do círculo

        # Contagem de pontos dentro e fora do círculo
        if z <= 1:  # Se o ponto estiver dentro do círculo
            N_in += 1
            if plot:
                ax.plot(x, y, 'o', color='blue')  # Pontos dentro do círculo
        else:
            if plot:
                ax.plot(x, y, 'o', color='pink')  # Pontos fora do círculo
        cont += 1

    
    pi_mc = 4 * N_in / N

    if verbose:  
        print('Número de pontos dentro: ', N_in)
        print('Número de pontos fora: ', N - N_in)
        print('Valor simulado de pi: ', pi_mc)
        print('Valor de pi: ', math.pi)
        print('Erro: ', pi_mc - math.pi)
        print('Precisão: ', 100 * (1 - abs(pi_mc - math.pi)), '%')
        print('Quantidade de iterações: ', cont)

    if plot:
        plt.show()

    return pi_mc

pi_montecarlo(N=100000, plot=True, verbose=True)
