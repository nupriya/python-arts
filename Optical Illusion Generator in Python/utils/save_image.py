import matplotlib.pyplot as plt

def save(fig, filename="output.png"):
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Saved as {filename}")