import numpy as np

def generate(ax):
    for r in range(20, 200, 20):
        theta = np.linspace(0, 2*3.1416, 200)
        
        for i in range(len(theta)-1):
            color = 'black' if i % 2 == 0 else 'white'
            x = r * np.cos(theta[i:i+2])
            y = r * np.sin(theta[i:i+2])
            ax.plot(x, y, color=color, linewidth=6)