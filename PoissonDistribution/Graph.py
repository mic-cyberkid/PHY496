import numpy as np
from matplotlib import pyplot as Graph

# grid size and parameters
nx, ny = 50, 50
dx, dy = 1.0, 1.0

# charge distribution
rho_values = np.zeros((nx, ny))
rho_values[nx // 2, ny // 2] = -1.0

# potential field ϕ with zero
phi_values = np.zeros((nx, ny))

# boundary conditions (Dirichlet: phi = 0 at the edges)
phi_values[:, [0, -1]] = 0  # Left and right boundaries
phi_values[[0, -1], :] = 0  # Top and bottom boundaries

# solution using Gauss-Seidel method
tolerance = 1e-5
max_iter = 5000

for it in range(max_iter):

    old_phi = phi_values.copy()

    # update points
    phi_values[1:-1, 1:-1] = 0.25 * (phi_values[2:, 1:-1] + phi_values[:-2, 1:-1] +
                              phi_values[1:-1, 2:] + phi_values[1:-1, :-2] - dx**2 * rho_values[1:-1, 1:-1])

    # check convergence
    if np.max(np.abs(phi_values - old_phi)) < tolerance:
        print(f"\033[32;1m[>] Converged after {it} iterations.")
        break

# Plot graph
Graph.figure(figsize=(8, 6))
Graph.imshow(phi_values, extent=[0, nx, 0, ny], origin='lower', cmap='gist_heat')
Graph.colorbar(label="Potential ϕ(x, y)")
Graph.title("Solution of Poisson's Equation using Finite Difference")
Graph.xlabel("x")
Graph.ylabel("y")
Graph.show()
