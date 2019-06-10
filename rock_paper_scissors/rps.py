#!/usr/bin/python

# Conditions
# Write a function that generates all possible plays that can be made in a game
# Your output should be a list of lists containing strings
# Each inner list should have length equal to the input n.
# 1 is to create a new list

import sys

def rock_paper_scissors(n):
  # list all possible plays
  plays = ['rock', 'paper', 'scissors']
  # initialize perms
  perms = []
  # nested recursive function with new args
  # and nonlocal access to perms
  def config_round(cur_round, rounds_left):
    # loop over the plays list
    for i in range (0, len(plays)):
      # append each play to the round list
      cur_round.append(plays[i])
      # if n was passed in as 0 initially, shortcircuit the recursion
      if rounds_left == 0:
        return perms.append([])
      # if this is the final round,append the list to perms
      elif rounds_left == 1:
        # append a copy to stop historic overrides of cur_round
        perms.append(cur_round[:])
      # if not the final round, run the cur_round again
      else:
        config_round(cur_round, rounds_left - 1)
      # remove last element of cur_round before for-loop starts
      del cur_round[-1]
  # invoke recursive function
  config_round([], n)
  return perms

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')