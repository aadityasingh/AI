# This program assists a human playing a game of ghost

input_file = "words.txt"

words = open(input_file).read().split('\n')
words.pop()

print("Hello! Welcome to ghost. Please take a moment to read the following rules for computer play.")
print("When prompted for your move, do one of the following: ")
print("1. Put in a lowercase letter if you wish to say a letter")
print("2. Put in an exclamation mark (!) if you wish to challenge")
print("3. Put in a hash tag (#) for a score check")
print("4. Put in a question mark (?) for a hint")
print("5. Put in a dollar sign ($) to cheat and find a definite win (DISCLAIMER: Only works sometimes for 2 players)")
print("6. When playing with more than 2 players, use the pipe (|) to get the best letter.")

trie = {}
poss_hash = {} 
for word in words:
  if len(word) > 3:
    current_hash = trie
    for l in word:
      current_hash = current_hash.setdefault(l, {})
    current_hash['!'] = '!'

  l = len(word)
  for i in range(l):
    before = word[:i]
    after = word[i:]
    if before in poss_hash:
      poss_hash[before].append(after)
    else:
      poss_hash[before] = [after]


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

def find_winning_letter(current_level):
  if '!' in current_level:
    return '!'

  for k in current_level:
    is_winning = True
    if '!' in current_level[k]:
      continue
    for m in current_level[k]:
      next_level = current_level[k][m]
      x = find_winning_letter(next_level)
      is_winning = is_winning & bool(x)
    if is_winning:
      return k

  return False

# bugged with 4 players...
def find_not_losing_letter(current_string, current_level, num_of_players):
  prob_hash = {}
  for k in current_level:
    if current_string+k in poss_hash:
      l = len(poss_hash[current_string + k])
      count = 0
      for rem_string in poss_hash[current_string + k]:
        if len(rem_string)%num_of_players == 0:
          count += 1
      prob_hash[(l-count)/l] = k
    elif k == '!':
      prob_hash[1] = k
    else:
      prob_hash[0] = k
  mp = max(prob_hash)
  return (mp, prob_hash[mp])

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
  actual_string = ''
  current_string = ""
  current_level = trie
  challenge_true = False
  turn_number = 0
  # The following while loop is used for one round
  while True:
    round_over = False
    # This for loop cycles through the players once
    for p in players:
      repeat = True
      # This final while loop is used to repeat the code in the case of a scorecheck
      while repeat:
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
          repeat = False
        elif next_char == '#':
          score_print(scores)
          repeat = True
        elif next_char == "?":
          print()
          to_print = "		Possible options: "
          possible_letters = []
          for k in current_level.keys():
            if k != "!":
              possible_letters.append(k)
          possible_letters = sorted(possible_letters)
          for l in possible_letters:
          	to_print += l
          print(to_print)
          print()
          repeat = True
        elif next_char == "$":
          print()
          to_print = "    Winning letter: "
          winning_letter = find_winning_letter(current_level)
          if winning_letter:
            to_print += winning_letter
          else:
            to_print = "    There is no definite win. Cheating doesn't always work :P"
          print(to_print)
          print()
          repeat = True
        elif next_char == "|":
          print()
          to_print = "    Best letter: "
          winning_letter = find_not_losing_letter(actual_string, current_level, len(players))
          to_print += winning_letter[1] + " with probability " + str(winning_letter[0])
          print(to_print)
          print()
          repeat = True
        elif next_char in 'abcdefghijklmnopqrstuvwxyz' and len(next_char) == 1:
          actual_string += next_char
          current_string += next_char + '-'
          if next_char in current_level:
            current_level = current_level[next_char]
            if '!' in current_level:
              challenge_true = True
            else:
              challenge_true = False
          else:
            challenge_true = True
          repeat = False
        else:
          print("Not a letter!")
          repeat = True
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


