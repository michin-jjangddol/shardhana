# tests/test_basic.py

import numpy as np
from scipy import linalg

def test_numpy_array_sum():
    arr = np.array([1, 2, 3])
    assert arr.sum() == 6

def test_scipy_eigenvalues():
    a = np.array([[1, 2], [3, 4]])
    eigvals = linalg.eigvals(a)
    # 고유값이 약 -0.372, 5.372 근처여야 함
    assert np.allclose(sorted(eigvals), sorted([-0.37228132, 5.37228132]), rtol=1e-3)
