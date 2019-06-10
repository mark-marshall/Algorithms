#!/usr/bin/python

import argparse

# Conditions
# Write a function find_max_profit that receives as input a list of stock prices. 
# Your function should return the maximum profit that can be made from a single buy and sell

def find_max_profit(prices):
  # set current_min_price_so_far to the first element
  current_min_price_so_far = prices[0]
  # set max_profit_so_far to the second element minu the first
  max_profit_so_far = prices[1] - prices[0]
  for i in range(1, len(prices)):
    # reset the max_profit_so_far if it changes
    if (prices[i] - current_min_price_so_far) > max_profit_so_far:
      max_profit_so_far = (prices[i] - current_min_price_so_far)
    # reset the current_min_price_so_far if it changes
    if prices[i] < current_min_price_so_far:
      current_min_price_so_far = prices[i]
  # return the max_profit_so_far
  return max_profit_so_far

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))