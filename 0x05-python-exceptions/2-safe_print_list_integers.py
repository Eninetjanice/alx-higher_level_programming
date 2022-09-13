#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index, i = 0, 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end='')
            i += 1
        except (ValueError, TypeError):
            pass
        else:
            index += 1
            i += 1
    print()
    return i
