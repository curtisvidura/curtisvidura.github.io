import numpy as np
import matplotlib.pyplot as plt
import math 
from IPython.display import display, Image
import latticegen
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


##### Making G - G

def tBLG(theta1, scale, res): 
    #theta1 angle between top and middle, theta angle between middle and bottom, scale is zoom, res is resolution-kinda

    a1 = 0.2464*scale  #graphene lattice constant
    r_k1=latticegen.transformations.a_0_to_r_k(a1, symmetry=6)  #reciprocal lattice vector

    kappa=1     #(float, default: 1) – strain/deformation magnitude. 1 corresponds to no strain.
    psi=0.      #(float, default: 0) – Principal strain direction with respect to horizontal.
    xi=0.

    lattice1 = latticegen.hexlattice_gen(r_k1, xi, res)                   #Graphene
    lattice2 = latticegen.hexlattice_gen(r_k1, theta1+xi, res)             #Graphene
    lattice3 = latticegen.hexlattice_gen(r_k1, theta2+xi, res)             #Graphene
    
    data = (lattice1 + lattice2 + lattice3).compute()
    return(data)

##### Making hBN - G


def BNG(theta1, scale, res): 

    a1 = 0.2464*scale  #graphene lattice constant
    a2 = 0.2504*scale  #hBN lattice constant

    r_k1=latticegen.transformations.a_0_to_r_k(a1, symmetry=6)  #reciprocal lattice vector
    r_k2=latticegen.transformations.a_0_to_r_k(a2, symmetry=6)
    
    kappa=1     #(float, default: 1) – strain/deformation magnitude. 1 corresponds to no strain.
    psi=0.      #(float, default: 0) – Principal strain direction with respect to horizontal.
    xi=0.

    lattice1 = latticegen.hexlattice_gen(r_k1, xi, res)                   #Graphene
    lattice2 = latticegen.hexlattice_gen(r_k2, theta1+xi, res)             #hBN
    
    data = (lattice1 + lattice2).compute()
    return(data)


##### Making G - G - G

def tTLG(theta1, theta2, scale, res): 
    #theta1 angle between top and middle, theta angle between middle and bottom, scale is zoom, res is resolution

    a1 = 0.2464*scale  #graphene lattice constant
    r_k1=latticegen.transformations.a_0_to_r_k(a1, symmetry=6)  #reciprocal lattice vector

    kappa=1     #(float, default: 1) – strain/deformation magnitude. 1 corresponds to no strain.
    psi=0.      #(float, default: 0) – Principal strain direction with respect to horizontal.
    xi=0.

    lattice1 = latticegen.hexlattice_gen(r_k1, xi, res)                   #Graphene
    lattice2 = latticegen.hexlattice_gen(r_k1, theta1+xi, res)             #Graphene
    lattice3 = latticegen.hexlattice_gen(r_k1, -theta2+xi, res)             #Graphene
    
    data = (lattice1 + lattice2 + lattice3).compute()
    return(data)


##### Making BN - G - BN

def BNGBN(theta1, theta2, scale, res): 
    #theta1 angle between top and middle, theta angle between middle and bottom, scale is zoom, res is resolution-kinda

    a1 = 0.2464*scale  #graphene lattice constant
    
    r_k1=latticegen.transformations.a_0_to_r_k(a1, symmetry=6)  #reciprocal lattice vector

    kappa=1     #(float, default: 1) – strain/deformation magnitude. 1 corresponds to no strain.
    psi=0.      #(float, default: 0) – Principal strain direction with respect to horizontal.
    xi=0.

    lattice1 = latticegen.hexlattice_gen(r_k1, xi, res)                   #Graphene
    lattice2 = latticegen.hexlattice_gen(r_k1, theta1+xi, res)             #Graphene
    lattice3 = latticegen.hexlattice_gen(r_k1, -theta2+xi, res)             #Graphene
    
    data = (lattice1 + lattice2 + lattice3).compute()
    return(data)

##### Making G - G - G

def tTLG(theta1, theta2, scale, res): 
    #theta1 angle between top and middle, theta angle between middle and bottom, scale is zoom, res is resolution-kinda

    a1 = 0.2464*scale  #graphene lattice constant

    r_k1=latticegen.transformations.a_0_to_r_k(a1, symmetry=6)  #reciprocal lattice vector

    kappa=1     #(float, default: 1) – strain/deformation magnitude. 1 corresponds to no strain.
    psi=0.      #(float, default: 0) – Principal strain direction with respect to horizontal.
    xi=0.

    lattice1 = latticegen.hexlattice_gen(r_k1, xi, res)                   #Graphene
    lattice2 = latticegen.hexlattice_gen(r_k1, theta1+xi, res)             #Graphene
    lattice3 = latticegen.hexlattice_gen(r_k1, theta2+xi, res)             #Graphene
    
    data = (lattice1 + lattice2 + lattice3).compute()
    return(data)

def showtTLG(theta1, theta2, scale, res):
    fig, ax = plt.subplots(figsize=[10,10])

    im= ax.imshow((tTLG(theta1,theta2, scale, res).T))

ax.set_title(f'TWISTEDTRILAYER \n $\\theta_1 = {theta1:.2f}^\\circ, \\theta_2 = {theta2:.2f}^\\circ$, Scale = x{scale}');
    
interact(showtTLG, theta1=(-5,5,0.01), theta2=(-5,5,0.01), scale=(1,100,1), res=(1,3,1))

get_ipython().run_line_magic('history', '')
