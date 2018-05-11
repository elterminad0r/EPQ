"""
Generating a (binary) Hadamard matrix
"""

import sys
import time
import argparse

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iterations", type=int,
                            help="Number of iterations to perform on matrix")
    parser.add_argument("--dump", type=argparse.FileType("w"), default="-",
                            help="File to write Hadamard matrix to")
    parser.add_argument("--verbose", action="store_true",
                            help="Write diagnostic information to stderr")
    parser.add_argument("--pretty", action="store_true",
                            help="Use visual block character to display 1")
    return parser.parse_args()

def prettify(had_mat, t_char="x", f_char=" "):
    return "\n".join("".join(t_char if i else f_char for i in row)
                                                     for row in had_mat)

def hadamard_iterate(mat):
    for r_ind in range(len(mat)):
        mat.append(mat[r_ind] * 2)
        mat[r_ind].extend([not i for i in mat[r_ind]])

def get_matrix(iterations, verbose=False):
    start = time.time()
    had_mat = [[1]]
    for i in range(iterations):
        hadamard_iterate(had_mat)
        if verbose:
            sys.stderr.write("iteration {} successful at {:.3f}s"
                                    .format(i, time.time() - start))
    for r_ind in range(len(had_mat)):
        had_mat.append([not i for i in had_mat[r_ind]])
    return had_mat

if __name__ == "__main__":
    args = get_args()
    display_chars = "10"
    if args.pretty:
        display_chars = "\u2588\u2588", "  "
    print(prettify(get_matrix(args.iterations, args.verbose), *display_chars),
          file=args.dump)
