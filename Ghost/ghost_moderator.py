# This program moderates a game of ghost

import time

input_file = "words.txt"

words = open(input_file).read().split('\n')

print("Hello! Welcome to ghost. Please take a moment to read the following rules for computer play.")
print("When prompted for your move, do one of the following: ")
print("1. Put in a lowercase letter if you wish to say a letter")
print("2. Put in an exclamation mark (!) if you wish to challenge")
print("3. Put in a question mark (?) for a score check")

tree = {} # a: {b: {stuff}, c: {stuff}... etc.}
poss_hash = {} # "ab": {"ack", "acus"}, etc.
for word in words:
  l = len(word)
  for i in range(l):
  	  

print("Okay! Let's get started!")