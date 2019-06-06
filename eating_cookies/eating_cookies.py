#!/usr/bin/python

# Conditions
# Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time
# If he were given n cookies, how many ways could he eat all cookies in the jar?

import sys

def eating_cookies(n):
  # set cache with 0s
  c = [0 for _ in range(n+1)]
  # nest recursive fn to receive updating cache
  def eating_perms(n, c):
    # base cases according to rules
    if n < 0:
      return 0
    elif n <= 1:
      return 1
    # grab value from cache if it exists
    elif c[n] > 0:
      return c[n]
    else:
      # set value in cache
      c[n] = eating_perms(n-1, c) + eating_perms(n-2, c) + eating_perms(n-3, c)
      return c[n]
  # return result from invocation of nested fn
  return eating_perms(n, c)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')