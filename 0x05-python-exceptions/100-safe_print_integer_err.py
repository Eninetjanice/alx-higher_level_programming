# #!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    while value is int:
        try:
            print("{:d}".format(value))
            return True
        except TypeError:
            print("Exception: ", sys.exc_info())
            return False
