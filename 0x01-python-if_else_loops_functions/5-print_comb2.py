#!/usr/bin/python3
for i in range(0, 100):
    if i < 100:
        print("{0:02d}".format(i), end=", ")
    else:
        print("{:d}".format(99))
