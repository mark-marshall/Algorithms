#!/usr/bin/python

# Conditions
# Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time
# If he were given n cookies, how many ways could he eat all cookies in the jar?

import sys

def eating_cookies(n):
  # base cases according to rules
  if n < 0:
    return 0
  elif n == 0 or n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  # move towards base cases via 3 possible cookie denominations
  return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')