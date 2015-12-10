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


print("Okay! Let's get started!")



