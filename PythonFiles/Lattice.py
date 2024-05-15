import numpy as np
import matplotlib.pyplot as plt

import latticegen

lattice = latticegen.anylattice_gen(r_k=0.01, theta=0,
                                    order=1, symmetry=4)
plt.imshow(lattice.T)