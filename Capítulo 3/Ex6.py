import numpy as np
import matplotlib.pyplot as plt

dom= np.linspace(-1,2,1000)
f= dom*np.exp(-dom**2) - 0.1
"""
xold= 0
TOL= 1e-10
while abs((xold*np.exp(-xold**2) - 0.1)) >= TOL:
  deno= (-2*xold**2 + 1) * np.exp(-xold**2)
  if abs(deno) >= TOL:



    xnew= xold - (xold*np.exp(-xold**2) - 0.1)/(deno)

    xold=xnew

    print(xnew)
"""
plt.plot(dom,f)
plt.show()