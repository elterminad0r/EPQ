#!/usr/bin/env python3

"""
Generates Postscript file that draws a Hadamard Matrix with filled in boxes.
This is a Python script that uses the other Python program to generate a
Hadamard matrix, and then inserts it into the premade Postscript template
"hadamard_template.ps", which knows how to draw it.
"""

# library used to parse the user's arguments. Basically, helps provide an
# interface to the program for the user
import argparse

# Regular Expression library. Is used to process text, in "is_ps_comment"
import re

# Operating System Path library. Used to find the location of the "template"
# file.
import os.path

# re-use the code in the "get_matrix" function
from hadamard_matrix import get_matrix

def is_ps_comment(line):
    """
    Determine if a line of code is a comment.  r"^\s*%(?:[^!%]|$)" is a "regular
    expression" that tells the computer to ignore any line that starts with a
    single % not followed by ! (a comment)
    """
    return re.match(r"^\s*%(?:[^!%]|$)", line)

# generates full path of template location
TEMPLATE_LOCATION = os.path.join(os.path.dirname(__file__),
                                 "hadamard_template.ps")

# Load the Postscript template to add data to
with open(TEMPLATE_LOCATION, "r") as psfile:
    PS_SOURCE = "".join(line for line in psfile if not is_ps_comment(line))

def get_args():
    """
    Interpret the user's arguments:
    - How many iterations should be performed
    - Where to write the generated Postscript to
    """
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
