#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_num = ((number * -1) % 10) * -1
else:
    last_num = number % 10
str1 = "Last digit of"
str2 = "is"
if last_num > 5:
    print("{} {} {} {} and is greater than 5"
          .format(str1, number, str2, last_num))
elif last_num == 0:
    print("{} {} {} {} and is 0".format(str1, number, str2, last_num))
elif (last_num < 6) and (last_num != 0):
    print("{} {} {} {} and is less than 6 and not 0"
          .format(str1, number, str2, last_num))
