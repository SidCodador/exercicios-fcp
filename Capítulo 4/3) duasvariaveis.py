import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def f(x,y):
    return np.cos(x)*np.sin(y)

def gradiente_f(x, y):
    df_dx = -np.sin(x) * np.sin(y) 
    df_dy = np.cos(x) * np.cos(y)   
    return df_dx, df_dy

x = np.linspace(-np.pi, np.pi, 100)  
y = np.linspace(-np.pi, np.pi, 100)
x,y= np.meshgrid(x,y)
z= f(x,y)
df_x, df_y= gradiente_f(x,y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = ax.plot_surface(x, y, z, cmap='nipy_spectral', edgecolor='k')
fig.colorbar(a) 

ax.set_title("Função f(x, y) = cos(x)cos(y)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Valores de f(x, y)")
plt.show()

#####################################################

plt.figure()
plt.contourf(x, y, z, levels=20, cmap='nipy_spectral')
plt.title('Curvas de nível de f(x, y) = cos(x)cos(y)')
plt.show()

###################################################

#plt.contourf(x, y, z, levels=20, cmap="nipy_spectral")
plt.quiver(x, y, df_x, df_y, color="black", scale=40)
plt.title("Gradiente de f(x, y) = cos(x)cos(y)")
plt.show()






