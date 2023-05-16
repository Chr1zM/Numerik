# -*- coding: utf-8 -*-
"""
Blatt06 Hilfsfunktionen
"""
import numpy as np
import matplotlib.pyplot as plt


from scipy.sparse import spdiags
import matplotlib.animation as animation  


def system(m):
    n = m*m
    
    e = np.ones(n)
    l = np.ones(n)
    l[m-1::m] = 0.0
    r = np.ones(n)
    r[::m] = 0.0
    
    A = spdiags([-e, -l, 4.0*e, -r, -e], [-m, -1, 0, 1, m], n, n, format='csr')
    
    b = -e / float(n)
    
    return A, b


def plotxk(xk):
    n = len(xk)
    m = int(np.sqrt(n))
    
    h = np.linspace(0, 1, m)
    yy,xx = np.meshgrid(h,h)
    
    fig = plt.figure('xk, m = {0}'.format(m))
    ax  = fig.gca(projection='3d')
    
    surf = ax.plot_surface(xx, yy, xk.reshape(m,m), cmap = plt.cm.jet, rstride = 5, cstride = 5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("Hoehe")
    plt.colorbar(surf)
    

def Ablock(m):
    # Blockmatrix fuerr 2d-Laplace
    n = m*m
    
    e = np.ones(n)
    l = np.ones(n)
    l[m-1::m] = 0.0
    r = np.ones(n)
    r[::m] = 0.0
    
    A = spdiags([-e, -l, 4.0*e, -r, -e], [-m, -1, 0, 1, m], n, n, format='csr')
    
    return A.toarray()
    

def ew_exakt(m):
    # exakte Eigenwerte fuer 2d-Laplace Blockmatrix, absteigend sortiert
    ew1d = 2.0 * (1.0 - np.cos( (np.arange(m) + 1.0) * np.pi / (m + 1.0) ))

    ew = (np.c_[ew1d] + ew1d).flatten()
    ew.sort()
    
    return ew[::-1]


def plotev(xk):
    # Eigenvektoren fuer 2d-Laplace Blockmatrix graphisch darstellen
    n = len(xk)
    m = int(np.sqrt(n))
    
    h = np.linspace(0, 1, m)
    yy,xx = np.meshgrid(h,h)
    
    fig = plt.figure()
    ax  = plt.subplot(projection='3d')
    
    surf = ax.plot_surface(xx, yy, xk.reshape(m,m), cmap = plt.cm.jet, rstride = 1, cstride = 1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("Hoehe")
    plt.colorbar(surf)


def animev(xk):
    # Eigenvektoren fuer 2d-Laplace Blockmatrix animieren
    n = len(xk)
    m = int(np.sqrt(n))
    
    h = np.linspace(0, 1, m)
    yy,xx = np.meshgrid(h,h)
    zz    = xk.reshape(m,m)
    
    zmax = 1.1 * abs(zz).max()
    
    def a(nf = 100, inter = 100, rep = False):
        fig = plt.figure()
        ax = plt.subplot(projection='3d')
        ax.set_axis_off()
        ax.grid(False)
        
        surf = ax.plot_surface(xx, yy, zz, cmap = plt.cm.jet, rstride = 1, cstride = 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("Hoehe")
        #colorbar(surf)
        
        ax.set_zlim(-zmax, zmax)
        
        def update(i, ax, fig):
            ax.cla()
            phi = i * 180.0 / np.pi / nf
            zzi = np.cos(phi) * zz
            wframe = ax.plot_surface(xx, yy, zzi, cmap = plt.cm.jet, rstride = 1, cstride = 1)
            ax.set_zlim(-zmax, zmax)
            ax.set_axis_off()
            ax.grid(False)
            return wframe,
        
        return animation.FuncAnimation(fig, update, 
                frames = range(nf), 
                fargs  = (ax, fig), interval = inter, repeat = rep)
        
    return a