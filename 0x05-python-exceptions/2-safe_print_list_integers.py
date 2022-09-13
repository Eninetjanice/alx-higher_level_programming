#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    index = 0
    i = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end='')
            i += 1
        except (ValueError, TypeError):
            pass
        except (IndexError):
            i += 1
        index += 1
    print()
    return i
