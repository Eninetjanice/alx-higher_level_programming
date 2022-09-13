#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    index = 0
    i = 0
    while index is not x:
        try:
            print("{:d}".format(my_list[i]), end='')
            index += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            index += 1
        i += 1
    print()
    return index
