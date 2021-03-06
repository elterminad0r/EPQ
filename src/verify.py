#!/usr/bin/env python2

"""
Verifies that the input is in (lexicographical) ascending order
"""

# imports "sys" library, used to either exit cleanly or display that there is a
# problem. it also communicates with other programs.
import sys

if __name__ == "__main__":
    cur_line = next(sys.stdin)
    for line in sys.stdin:
        if cur_line > line:
            print("error: {!r} > {!r}".format(cur_line, line))
            sys.exit(1)
        cur_line = line
