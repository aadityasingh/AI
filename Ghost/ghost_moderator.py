# This program moderates a game of ghost

input_file = "words.txt"

words = open(input_file).read().split('\n')
words.pop()

print("Hello! Welcome to ghost. Please take a moment to read the following rules for computer play.")
print("When prompted for your move, do one of the following: ")
print("1. Put in a lowercase letter if you wish to say a letter")
print("2. Put in an exclamation mark (!) if you wish to challenge")
print("3. Put in a question mark (?) for a score check")

trie = {} 
for word in words:
  if len(word) > 3:
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

def score_print(scores):
  print("SCORECHECK-------------------------------")
  for player in scores:
    print("Player #" + str(player) + ": " + "GHOST"[:scores[player]])
  print("-----------------------------------------")

def player_lost(players, scores):
  for player in players:
    if scores[player] == 5:
      return [True, player]
  return [False]


print("Okay! Let's get started!")
num = input("How many people are playing: ")
num_of_players = int(num)
winner = False
scores = {}
players = []
dead_players = []
for i in range(num_of_players):
  scores[i+1] = 0
  players.append(i+1)

round_num = 1
# The following while loop is used for the whole game
while True:
  print("Round #" + str(round_num))
  current_string = ""
  current_level = trie
  challenge_true = False
  turn_number = 0
  # The following while loop is used for one round
  while True:
    round_over = False
    # This for loop cycles through the players once
    for p in players:
      scorecheck = True
      # This final while loop is used to repeat the code in the case of a scorecheck
      while scorecheck:
        print("The current string is: '" + current_string + "'")
        next_char = input("Player " + str(p) + ": ")
        if next_char == '!':
          if challenge_true:
            index_to_get_a_point = players.index(p) - 1
            if index_to_get_a_point == -1: index_to_get_a_point = len(players) - 1
            print("Your challenge is correct.")
            scores[players[index_to_get_a_point]] += 1
            score_print(scores)
          else:
            print("Your challenge is incorrect.")
            scores[p] += 1
            score_print(scores)
          round_over = True
          scorecheck = False
        elif next_char == '?':
          score_print(scores)
          scorecheck = True
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
          scorecheck = False
      if round_over:
        break
    if round_over:
      break


  arr = player_lost(players, scores)
  if arr[0]:
    print("Player #" + str(arr[1]) + " has lost the game")
    players.remove(arr[1])
    dead_players.append(arr[1])
  if len(players) == 1:
    winner = players.pop()
  if winner:
    print("This game of ghost is over. The rankings are shown below: ")
    print("1. Player " + str(winner))
    i = len(dead_players) - 1
    x = 2
    while i > -1:
      print(str(x) + ". Player " + str(dead_players[i]))
      i -= 1
      x += 1
    break
  round_num += 1


  