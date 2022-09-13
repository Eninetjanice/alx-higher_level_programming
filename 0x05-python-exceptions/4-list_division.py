#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i, newlist = 0, []
    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by o")
        except IndexError:
            print("out of range")
        finally:
            newlist.append(result)
            i += 1
    return newlist
