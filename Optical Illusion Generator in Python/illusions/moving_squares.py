import numpy as np
import matplotlib.pyplot as plt

def generate():
    size = 10
    grid = 12
    img = np.zeros((grid*size, grid*size))

    for i in range(grid):
        for j in range(grid):
            shift = int(size * 0.3) if (i + j) % 2 == 0 else -int(size * 0.3)
            x, y = i * size, j * size
            img[x:x+size, y+shift:y+size+shift] = 1

    return img