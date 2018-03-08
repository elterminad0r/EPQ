import time

def prettify(had_mat):
    return "\n".join("".join("x" if i else " " for i in row) for row in had_mat)

def hadamard_iterate(mat):
    for r_ind in range(len(mat)):
        mat.append(mat[r_ind] * 2)
        mat[r_ind].extend([not i for i in mat[r_ind]])

had_mat = [[1]]

start = time.time()
for i in range(20):
    hadamard_iterate(had_mat)
    print("iteration {} successful at {:.3f}s".format(i, time.time() - start))
