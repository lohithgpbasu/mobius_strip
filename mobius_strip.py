import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R=1, w=0.2, n=100):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self._compute_points()

    def _compute_points(self):
        U, V = self.U, self.V
        R = self.R
        X = (R + V * np.cos(U / 2)) * np.cos(U)
        Y = (R + V * np.cos(U / 2)) * np.sin(U)
        Z = V * np.sin(U / 2)
        return X, Y, Z

    def surface_area(self):
        du = 2 * np.pi / self.n
        dv = self.w / self.n
        dA = np.zeros_like(self.U)

        # Cross product of partial derivatives for surface area
        for i in range(self.n - 1):
            for j in range(self.n - 1):
                r1 = np.array([
                    self.X[i+1, j] - self.X[i, j],
                    self.Y[i+1, j] - self.Y[i, j],
                    self.Z[i+1, j] - self.Z[i, j]
                ])
                r2 = np.array([
                    self.X[i, j+1] - self.X[i, j],
                    self.Y[i, j+1] - self.Y[i, j],
                    self.Z[i, j+1] - self.Z[i, j]
                ])
                dA[i, j] = 0.5 * np.linalg.norm(np.cross(r1, r2))
        return np.sum(dA)

    def edge_length(self):
        # Approximate length of the boundary (2 loops)
        top_edge = np.array([
            (self.X[-1, i], self.Y[-1, i], self.Z[-1, i]) for i in range(self.n)
        ])
        bottom_edge = np.array([
            (self.X[0, i], self.Y[0, i], self.Z[0, i]) for i in range(self.n)
        ])
        length = 0
        for edge in [top_edge, bottom_edge]:
            for i in range(len(edge) - 1):
                length += np.linalg.norm(np.array(edge[i+1]) - np.array(edge[i]))
        return length

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, color='skyblue', edgecolor='gray', alpha=0.8)
        ax.set_title("Möbius Strip")
        plt.show()


if __name__ == "__main__":
    R = float(input()) # Takes input distance from the center to the strip (for eg:- 1, 2.5, 5.75....)
    w = float(input()) # Takes strip width (for eg:- 0.6, 0.4, 0.5....)
    n = int(input()) # Takes number of points in the mesh (for eg:- 20, 50, 100...)
    strip = MobiusStrip(R, w, n)
    print("Surface Area ≈", strip.surface_area())
    print("Edge Length ≈", strip.edge_length())
    strip.plot()
