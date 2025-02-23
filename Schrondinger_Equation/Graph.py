import numpy as np
from matplotlib import pyplot as Graph
import numba
from numba import jit
from scipy.linalg import eigh_tridiagonal

# define parameters

Nt = 100000
Nx = 301
dx = 1/(Nx-1)
dt = 1e-7

x = np.linspace(0, 1, Nx)
psi0 = np.sqrt(2)*np.sin(np.pi*x)
mu, sigma = 1/2, 1/20
V = -1e4*np.exp(-(x-mu)**2/(2*sigma**2))


# plot graph
Graph.figure(figsize=(8,3))
Graph.plot(x,V)
Graph.xlabel('$x$')
Graph.ylabel('$V(x)$')
Graph.grid()
Graph.show()

psi = np.zeros([Nt,Nx])
psi[0] = psi0

@numba.jit("c16[:,:](c16[:,:])", nopython=True, nogil=True)
def compute_psi(psi):
    for t in range(0, Nt-1):
        for i in range(1, Nx-1):
            psi[t+1][i] = psi[t][i] + 1j/2 * dt/dx**2 * (psi[t][i+1] - 2*psi[t][i] + psi[t][i-1]) - 1j*dt*V[i]*psi[t][i]

        normal = np.sum(np.absolute(psi[t+1])**2)*dx
        for i in range(1, Nx-1):
            psi[t+1][i] = psi[t+1][i]/normal

    return psi

psi_fdm = compute_psi(psi.astype(complex))

Graph.plot(x, np.absolute(psi_fdm[10000])**2)
Graph.grid()
Graph.show()
