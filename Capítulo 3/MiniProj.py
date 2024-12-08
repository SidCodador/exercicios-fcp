import numpy as np  
from scipy.integrate import quad  
import matplotlib.pyplot as plt  

L = 1  
Tensao = 2  
g = 9.81  


def rho(x):
    return 1  
def rho2(x):
    return 0.5 * (1 + np.exp(-100 * (x - 0.5)**2))  


def acharMassas(rhoUtilizado, N):
    pesos = []  
    massas =[]
    Lo = L / N  
    for i in range(N-1):
        if i == 0:  #primeira particula
            a = 0
            b = 3 * Lo / 2
        elif i == N - 2:  #ultima particula
            a = L - 3 * Lo / 2
            b = L
        else:  #outrs particulas
            a = (i + 1) * Lo - Lo / 2
            b = (i + 1) * Lo + Lo / 2

        massa, _ = quad(rhoUtilizado, a, b)  
        peso = -massa * g  
        massas.append(massa)
        pesos.append(peso)  
    a = sum(massas)
    print(a)
    return pesos 


def aumentarForca(i, Nova, iniciais):
    iniciais[i] += Nova
    return iniciais



def jacobi(N, rho_):
    iniciais = [0] * (N-1)  
    Lo = L / N  

    ysold = np.random.rand(N-1) 
    g = 9.8

    tol = 1e-5  
    maxit = 10000  
    err = 10 * tol  
    iter = 0  

    ynew = np.zeros(N-1)  
    pesos = acharMassas(rho_, N)  

    while iter < maxit and err > tol:
        for i in range(N-1):
            yi_prev = ysold[i-1] if i > 0 else 0
            yi_next = ysold[i+1] if i < N-2 else 0
            ynew[i] = 0.5 * (yi_prev + yi_next + (Lo / Tensao) * (iniciais[i] + pesos[i]))


        err = np.linalg.norm(ynew - ysold)  
        ysold = ynew.copy()
        iter += 1

    return ysold



def gauss_Seidel(N, rho_):
    Lo = L / N 
    g = 9.8  

    iniciais = [0] * (N-1)  
    pesos = acharMassas(rho_, N)  

    #aumentarForca(39, -2, iniciais)
    aumentarForca(17, 2, iniciais)
    aumentarForca(30, -2, iniciais)

    B = np.zeros((N-1, N-1))
    for i in range(N-1):
        B[i, i] = 2 * Tensao / Lo  
        if i > 0:
            B[i, i-1] = -Tensao / Lo  
        if i < N-2:
            B[i, i+1] = -Tensao / Lo  

    b = np.array(pesos) + iniciais 

    yold = np.random.rand(N-1) 

    tol = 1e-5  
    maxit = 100000  
    iter = 0  

    
    for k in range(maxit):
        ynew = yold.copy()  

        for i in range(len(b)):
            alfa = np.dot(B[i, :i], ynew[:i]) + np.dot(B[i, i+1:], yold[i+1:])
            ynew[i] = (b[i] - alfa) / B[i, i]

        if np.linalg.norm(ynew - yold) < tol:
            return yold

        yold = ynew  


y1_rho = jacobi(80, rho)
y2_rho = gauss_Seidel(80, rho)
y1_rho2 = jacobi(80, rho2)
y2_rho2 = gauss_Seidel(80, rho2)

x_rho = np.linspace(0, L, len(y1_rho))
x_rho2 = np.linspace(0, L, len(y1_rho2))

plt.plot(x_rho, y1_rho, label='Jacobi (rho)')
plt.plot(x_rho, y2_rho, label='Gauss-Seidel (rho)')

plt.plot(x_rho2, y1_rho2, label='Jacobi (rho2)')
plt.plot(x_rho2, y2_rho2, label='Gauss-Seidel (rho2)')

plt.grid(True)
plt.legend()
plt.xlabel("Posição na corda")
plt.ylabel("Deslocamento")
plt.title("Deslocamento da corda para diferentes densidades")
plt.show()



def jacobi2Forca(N, rho_, i):

  iniciais=[0] * (N-1) 
  Lo= L/N

  posicoes= []

  g= 9.8

  aumentarForca(38,i,iniciais)

  pesos= acharMassas(rho_, N)
  B= np.zeros((N-1, N-1))

  for i in range(N-1):
    B[i,i] = 2* Tensao / Lo
    
    if i > 0:
      B[i,i-1] = -Tensao / Lo
    
    if i < N-2:
      B[i, i+1] = -Tensao / Lo
  
  b= np.array(pesos) + iniciais

  O= np.diag(np.diag(B))
  P= np.tril(B, -1)
  U= np.triu(B, 1)

  yold= np.random.rand(N-1)

  tol= 1e-5
  maxit= 10000
  err= 10 * tol
  iter= 0
  
  while err > tol and iter < maxit:

    ynew= np.linalg.inv(O) @ (b - (P+U) @ yold)
    err= np.linalg.norm(ynew-yold)
    yold=ynew
    iter+=1

  return yold[38]



forcas= [-1, -2, -3, -4, -5, -6, -7,-8,-9,-10]
posicoes39= []
for i in forcas:
    a= jacobi2Forca(80,rho,i)
    posicoes39.append(a)

plt.plot(forcas,posicoes39)
plt.show()




