import numpy as np
from matplotlib import pyplot as plt


def cami2d(n):
    xs = [0]
    ys = [0]
    b = [0, 1, 2, 3]
    for i in range(n):
        a = np.random.choice(b)
        if a == 0:
            xs.append(xs[i]+1)
            ys.append(ys[i])
        elif a == 1:
            xs.append(xs[i]-1)
            ys.append(ys[i])
        elif a == 2:
            xs.append(xs[i])
            ys.append(ys[i]+1)
        elif a == 3:
            xs.append(xs[i])
            ys.append(ys[i]-1)

    return xs, ys


def distancia2D(M, N):
    msd = np.zeros(N)

    for i in range(M):
        x, y = cami2d(N)

        for t in range(N):
            deslocamento = x[t]**2 + y[t]**2
            msd[t] += deslocamento

    msd /= M
    return msd


def cami3d(n):
    xs = [0]
    ys = [0]
    zs = [0]
    b = [0, 1, 2, 3, 4, 5]

    for i in range(n):
        a = np.random.choice(b)
        if a == 0:
            xs.append(xs[i]+1)
            ys.append(ys[i])
            zs.append(zs[i])
        elif a == 1:
            xs.append(xs[i]-1)
            ys.append(ys[i])
            zs.append(zs[i])
        elif a == 2:
            xs.append(xs[i])
            ys.append(ys[i]+1)
            zs.append(zs[i])
        elif a == 3:
            xs.append(xs[i])
            ys.append(ys[i]-1)
            zs.append(zs[i])
        elif a == 4:
            xs.append(xs[i])
            ys.append(ys[i])
            zs.append(zs[i]-1)
        elif a == 5:
            xs.append(xs[i])
            ys.append(ys[i])
            zs.append(zs[i]+1)

    return xs, ys, zs


def distancia3D(M, N):
    msd = np.zeros(N)

    for i in range(M):
        x, y, z = cami3d(N)

        for t in range(N):
            deslocamento = x[t]**2 + y[t]**2 + z[t]**2
            msd[t] += deslocamento
    msd /= M
    return msd


M = 100
N = 10**3
x2d, y2d = cami2d(N)
x3d, y3d, z3d = cami3d(N)

msd2D = distancia2D(M, N)
msd3D = distancia3D(M, N)

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x2d, y2d, label='Caminhada 2D')
ax1.set_title("Caminho Aleatório 2D")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.plot(x3d, y3d, z3d, label="Caminho 3D")
ax2.set_title("Caminho Aleatório 3D")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")

ax3 = fig.add_subplot(2, 1, 2)
ax3.plot(msd2D, label="MSD 2D")
ax3.plot(msd3D, label="MSD 3D")
ax3.set_title("Deslocamento Quadrático Médio (MSD)")
ax3.set_xlabel("Passos (t)")
ax3.set_ylabel("MSD (d²(t))")
ax3.legend()

plt.tight_layout()
plt.show()

