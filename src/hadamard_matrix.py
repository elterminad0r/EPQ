import numpy as np

class Matrix:
    def __init__(self, w, h):
        self.mat = [[0 for _ in range(h)] for _ in range(w)]

def hadamard_iteration(mat):
    return mat - mat
         + mat + mat
