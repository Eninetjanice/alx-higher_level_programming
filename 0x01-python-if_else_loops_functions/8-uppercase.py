#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            j = chr(ord(i) - 32)
        else:
            j = i
        result = result + j
    print("{}".format(result))
