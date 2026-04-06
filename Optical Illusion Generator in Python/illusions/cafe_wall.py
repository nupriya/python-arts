import matplotlib.pyplot as plt

def generate(ax):
    rows, cols = 12, 12
    block = 20

    for i in range(rows):
        for j in range(cols):
            x = j * block
            y = i * block
            
            if i % 2 == 0:
                x += block // 2
            
            color = 'black' if (i + j) % 2 == 0 else 'white'
            rect = plt.Rectangle((x, y), block, block, color=color)
            ax.add_patch(rect)