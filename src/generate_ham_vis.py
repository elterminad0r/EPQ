"""
Generates Postscript file that draws a Hadamard Matrix with filled in boxes.
"""

# library used to parse the user's arguments. Basically, helps provide an
# interface to the program for the user
import argparse

# Regular Expression library. Is used to process text, in "is_ps_comment"
import re

# re-use the code in the "get_matrix" function
from hadamard_matrix import get_matrix

# function that determines if a line of code is a comment.
# r"^\s*%(?:[^!%]|$)" is a "regular expression" that tells the computer to
# ignore any line that starts with a single % not followed by ! (a comment)
def is_ps_comment(line):
    return re.match(r"^\s*%(?:[^!%]|$)", line)

# Load the Postscript template to add data to
with open("hadamard_template.ps", "r") as psfile:
    PS_SOURCE = "".join(line for line in psfile if not is_ps_comment(line))

# function that handles given arguments
def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iterations", type=int,
                            help="number of Hadamard iterations")
    parser.add_argument("--dump", type=argparse.FileType("w"), default="-",
                            help="file to write generated postscript to")
    return parser.parse_args()

# when the program is run
if __name__ == "__main__":
    # get the user's arguments
    args = get_args()
    # generate a matrix
    mat = get_matrix(args.iterations)
    # insert the matrix in the template and write it to the output file
    args.dump.write(PS_SOURCE.replace("$HAD_MATRIX",
        "\n".join("[{}]".format(" ".join(str(int(i)) for i in row)) for row in mat)))
