import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

# Numpy
a = np.array([[1, 2], [3, 4]])
print("Numpy array:\n", a)

# Scipy
eigvals = linalg.eigvals(a)
print("Eigenvalues:", eigvals)

# Matplotlib
plt.plot([0, 1, 2], [0, 1, 4])
plt.title("Matplotlib Test Plot")
plt.savefig("test_plot.png")
print("Plot saved as test_plot.png")

