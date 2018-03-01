import numpy as np

def prettify(had_mat):
    return "\n".join(" ".join(str(int(i)) for i in row) for row in had_mat)

def hadamard_iterate(mat):
    for r_ind in range(len(mat)):
        mat.append(mat[r_ind] * 2)
        mat[r_ind].extend([not i for i in mat[r_ind]])

had_mat = [[1]]

for _ in range(5):
    hadamard_iterate(had_mat)
    print()
    print(prettify(had_mat))
