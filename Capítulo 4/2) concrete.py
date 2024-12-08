import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread('concrete.jpg')

#print(img)

v = img[:, :, 0]

plt.imshow(img)
plt.title('Imagem Original')
plt.show()

recortada = v[50:150, 50:150]

plt.imshow(recortada, cmap='gray')
plt.title('Janela Recortada')
plt.show()


recortada_normalizada = recortada/recortada.max()

limiar = 0.5
img = (recortada_normalizada>limiar)*1.0

plt.imshow(img, cmap='gray')
plt.title('Agregados Identificados')
plt.show()

#fracoes_agregados= []
limiares = [0.3, 0.5, 0.7]

for i in limiares:
    img = (recortada_normalizada>i) * 1.0
    fracao_agregados= img.sum()/img.size
    #fracoes_agregados.append(fracao_agregados)
    print(f'Limiar: {i}, Fração de agregados: {fracao_agregados:.2f}') 

'''
plt.plot(limiares, fracoes_agregados, marker='o')

plt.xlabel('Limiar')
plt.ylabel('Fração de Agregados')
plt.title('Fração de Agregados em Relação ao Limiar')
plt.grid(True)
'''
plt.show()

