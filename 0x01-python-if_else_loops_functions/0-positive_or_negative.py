#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
   print("{:d} Positive number" .format(number))
elif number == 0:
   print("{:d} Zero" .format(number))
else:
   print("{:d} Negative number" .format(number))
   