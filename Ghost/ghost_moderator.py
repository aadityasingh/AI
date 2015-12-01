# This program moderates a game of ghost

import time

input_file = "words.txt"

words = open(input_file).read().split('\n')
words.pop()

print("Hello! Welcome to ghost. Please take a moment to read the following rules for computer play.")
print("When prompted for your move, do one of the following: ")
print("1. Put in a lowercase letter if you wish to say a letter")
print("2. Put in an exclamation mark (!) if you wish to challenge")
print("3. Put in a question mark (?) for a score check")

trie = {} # a: {b: {stuff}, c: {stuff}... etc.}
poss_hash = {} # "ab": {"ack", "acus"}, etc.
for word in words:
  current_hash = trie
  for l in word:
    current_hash = current_hash.setdefault(l, {})
  current_hash['!'] = '!'

  # l = len(word)
  # for i in range(l):
  #   before = word[:i]
  #   after = word[i:]
  #   if before in poss_hash:
  #     poss_hash[before].append(after)
  #   else:
  #     poss_hash[before] = [after]


  	  

print("Okay! Let's get started!")
num = input("How many people are playing?")
num_of_players = str(num)
scores = {}
for i in range(num_of_players):
  scores[i+1] = ''

round_num = 1
while True:
  print("Round #" + str(round_num))
  current_string = ""
  current_level = trie
  challenge_true = False
  turn_number = 0
  while True:
    print("The current string is: '" + current_string + "'")
    next_char = input("Player " + str(turn_number%num_of_players +1) + ": ")
    if next_char == '!':
      if challenge_true:
        player_to_get_a_point = turn_number - 1
        if player_to_get_a_point == 0: player_to_get_a_point += num_of_players
        print("Your challenge is correct.")
        print("")
      else:
        #stuff
    elif next_char == '?':
      #stuff
    else:
      current_string += next_char + '-'
      if next_char in current_level:
        current_level = current_level[next_char]
        if '!' in current_level:
          challenge_true = True
        else:
          challenge_true = False
      else:
        challenge_true = True

    turn_number += 1


  