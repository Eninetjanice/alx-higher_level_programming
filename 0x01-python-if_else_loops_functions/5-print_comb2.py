#!/usr/bin/python3
for i in range(0, 99):
    if i < 99:
        print("{0:02d}".format(i), end=", ")
    else:
        print("{:d}".format(99))
