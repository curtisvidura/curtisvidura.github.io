import numpy as np
import matplotlib.pyplot as plt
import math 
import latticegen


a1 = 0.2464  #graphene lattice constant
a2 = 0.2504  #hBN lattice constant

r_k1=latticegen.transformations.a_0_to_r_k(a1, symmetry=6)  #reciprocal lattice vector
r_k2=latticegen.transformations.a_0_to_r_k(a2, symmetry=6)

theta=0     #angle  
kappa=1     #(float, default: 1) – strain/deformation magnitude. 1 corresponds to no strain.
psi=0.      #(float, default: 0) – Principal strain direction with respect to horizontal.
xi=0.

lattice1 = latticegen.hexlattice_gen(r_k1, xi, 1)
lattice2 = latticegen.hexlattice_gen(r_k2, theta+xi, 1,
                                     kappa=kappa, psi=psi)

fig, ax = plt.subplots(figsize=[10,10])


data = (lattice1 + lattice2).compute()
im = ax.imshow(data.T,
               vmax=np.quantile(data,0.95),
               vmin=np.quantile(data,0.05),
               )
ax.set_xlabel('x (nm)')
ax.set_ylabel('y (nm)')
ax.set_title(f'Graphene-hBN \n $\\theta = {theta:.2f}^\\circ, \\kappa = {kappa:.3f}, \\psi = {psi:.2f}^\\circ$');