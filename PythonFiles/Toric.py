print("This is my Toric Code file")

import numpy as np
import matplotlib as plt 


def generate_square_lattice(size):
    """
    Generate a square lattice of given size.

    Parameters:
    size (int): The size of the lattice (number of nodes along one dimension).

    Returns:
    np.array: A 2D array representing the square lattice.
    """
    lattice = np.zeros((size, size))
    return lattice

def plot_lattice(lattice):
    """
    Plot the square lattice.

    Parameters:
    lattice (np.array): The 2D array representing the square lattice.
    """
    size = lattice.shape[0]
    fig, ax = plt.subplots()
    for i in range(size):
        for j in range(size):
            ax.plot([i, i+1], [j, j], color='black')
            ax.plot([i, i], [j, j+1], color='black')
            if i == size - 1:
                ax.plot([i+1, i+1], [j, j+1], color='black')
            if j == size - 1:
                ax.plot([i, i+1], [j+1, j+1], color='black')

    ax.set_aspect('equal')
    plt.xlim(0, size)
    plt.ylim(0, size)
    plt.show()

# Example usage
size = 5  # Change this to generate a lattice of a different size
lattice = generate_square_lattice(size)
plot_lattice(lattice)