import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread('stinkbug.png')

n = 100
largura, comprimento, _ = img.shape
a = np.random.uniform(0, comprimento, size=n)
b = np.random.uniform(0, largura, size=n)

cores = ['black']*(n//2) + ['white']*(n//2)
np.random.shuffle(cores)

v = img[:, :, 0]

print(img.shape)

plt.scatter(a, b, color=cores)
imgplot = plt.imshow(v, cmap='plasma')
#imgplot = plt.imshow(v, cmap="nipy_spectral")
plt.colorbar()

##########################################

def suavizar(matriz):
    B = np.zeros_like(matriz)
    for i in range(1, matriz.shape[0] - 1):
        for j in range(1, matriz.shape[1] - 1):
            B[i, j]=(matriz[i, j]+matriz[i+1, j]+matriz[i-1, j]+matriz[i, j+1]+matriz[i, j-1])/5
    return B

n_iteracoes = 10
resultado = v

for _ in range(n_iteracoes):
    resultado = suavizar(resultado)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(v, cmap='Blues')
plt.title('Imagem Original')
plt.subplot(1, 2, 2)
plt.imshow(resultado, cmap='Blues')
plt.title(f'Imagem Suavizada ({n_iteracoes} Iterações)')
plt.show()

########################################

def suavizar2(matriz):
    C = np.zeros_like(matriz)
    for i in range(1, matriz.shape[0]-1):
        for j in range(1, matriz.shape[1]-1):
            C[i, j]=(matriz[i, j]+matriz[i+1, j]+matriz[i-1, j]+matriz[i, j+1]+matriz[i, j-1]
            +matriz[i+1, j+1]+ matriz[i+1, j-1]+ matriz[i-1, j-1]+ matriz[i-1, j+1])/9
    return C

nu_iteracoes = 10

for _ in range(nu_iteracoes):
    resultado = suavizar2(resultado)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(v, cmap='binary')
plt.title('Imagem Original')
plt.subplot(1, 2, 2)
plt.imshow(resultado, cmap='binary')
plt.title(f'Imagem Suavizada ({nu_iteracoes} Iterações)')
plt.show()