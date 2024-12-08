import numpy as np 
import random 
from matplotlib import pyplot as plt



def dados(M,N):
    resultados= []
    for i in range(N): #Quantidade de vezes jogadas
        b= (int(np.sum(np.random.randint(1,7, M)))) #Quantidade de dados jogados
        resultados.append(b)


    fig, (ax1,ax2)= plt.subplots(1,2)
    count, bins= np.histogram(resultados)    
    ax1.stairs(count, bins, fill=True)

    y= np.linspace(M, 6*M, 11)
    ax2.hist(resultados, bins=y, fill=True, edgecolor='black')


###### Counts é a quantidade de vezes que um numero foi registrado dentro de um intervalo (O resultado (soma) igual a 15 apareceu 200 vezes)
###### Bins é o proprio intevalo (4 a 6, 6 a 8, 8 a 10...)


    print(bins)

    plt.show()

dados(4,10000)








