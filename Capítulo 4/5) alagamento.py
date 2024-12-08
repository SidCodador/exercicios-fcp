import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def init_grid(N):
    grid = np.zeros((N, N), dtype=int)
    center = N // 2
    grid[center, center] = 1
    num_obstaculos = int(0.4 * N * N)
    num_obstaculos = np.random.choice(N * N, num_obstaculos, replace=False)
    for idx in num_obstaculos:
        x, y = divmod(idx, N)
        grid[x, y] = 2

    return grid


def update_grid(grid):
    N = grid.shape[0]
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            if grid[i, j] == 1:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and grid[ni, nj] == 0:
                        new_grid[ni, nj] = 1
    return new_grid


N = 50 
grid = init_grid(N)

fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(grid, cmap="viridis", interpolation="nearest")
ax.set_title("Algoritmo de Alagamento")
ax.set_xticks([])
ax.set_yticks([])

def update(frame):
    global grid
    grid = update_grid(grid)
    im.set_data(grid)
    return [im]

ani = FuncAnimation(fig, update, frames=100, interval=200, blit=True)
plt.show()
