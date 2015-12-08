# This program plays ghost with a human

# This program assists a human playing a game of ghost

input_file = "words.txt"

words = open(input_file).read().split('\n')
words.pop()

# print("Hello! Welcome to ghost. Please take a moment to read the following rules for computer play.")
# print("When prompted for your move, do one of the following: ")
# print("1. Put in a lowercase letter if you wish to say a letter")
# print("2. Put in an exclamation mark (!) if you wish to challenge")
# print("3. Put in a question mark (?) for a score check")
# print("4. Put in a dollar sign ($) for a hint")

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

def find_winning_letter(current_level, turn):
  if '!' in current_level:
    if turn == 0:
      return '!'
    else:
      return False

  for k in current_level:
    for m in current_level[k]:

  return False


print(find_winning_letter(trie['v']['a']['l']['u']['e'], 1))

