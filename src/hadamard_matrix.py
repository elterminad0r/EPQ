#!/usr/bin/env python3

"""
Generating a (binary) Hadamard matrix
"""

# imports the "system" library, which is used to write error messages to
# sys.stderr
import sys

# imports the "time" library, which is used to show diagnostic timing
# information (see get_matrix)
import time

# imports the "argparse" library, which is used to interpret the parameters
# given to the program by the user
import argparse

def get_args():
    """
    Use argparse to get:
    - The numbers of Hadamard iterations to perform
    - A file to store the resulting matrix in (they can get quite large)
    - Whether or not to show diagnostic timing
    - How to format the matrix
    """
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
    """
    Format a hadamard matrix nicely, using 'x' to represent a 1, by default.
    """
    return "\n".join("".join(t_char if i else f_char for i in row)
                                                     for row in had_mat)

def hadamard_iterate(mat):
    """
    Perform a Hadamard iteration on a matrix.
    """
    for r_ind in range(len(mat)):
        # add the current row the the end of the matrix, duplicated twice
        mat.append(mat[r_ind] * 2)
        # add the row's own inverse to its end
        mat[r_ind].extend([not i for i in mat[r_ind]])

def get_matrix(iterations, verbose=False):
    """
    Generate a full Hadamard matrix given number of iterations
    """
    # the start time
    start = time.time()
    # the initial matrix
    had_mat = [[1]]
    # iterate the appropriate number of times
    for i in range(iterations):
        hadamard_iterate(had_mat)
        # if the user wants to know, provide diagnostic information
        if verbose:
            sys.stderr.write("iteration {} successful at {:.3f}s"
                                    .format(i, time.time() - start))
    # Finally, append -M to the bottom of M
    for r_ind in range(len(had_mat)):
        had_mat.append([not i for i in had_mat[r_ind]])
    return had_mat

# if the script is called directly, generate a matrix and format and write it
# as specified
if __name__ == "__main__":
    args = get_args()
    display_chars = "10"
    if args.pretty:
        display_chars = "\u2588\u2588", "  "
    print(prettify(get_matrix(args.iterations, args.verbose), *display_chars),
          file=args.dump)
