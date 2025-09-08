# tests/test_basic.py
import numpy as np
from scipy import linalg

def test_numpy_array():
    a = np.array([[1, 2], [3, 4]])
    assert a.shape == (2, 2)
    assert a.sum() == 10

def test_scipy_eigenvalues():
    a = np.array([[1, 2], [3, 4]])
    eigvals = linalg.eigvals(a)
    # 고유값 2개가 나와야 한다
    assert len(eigvals) == 2
