from time import time
import pickle

# Opens the pickle file nbrs.pkl
f = open('nbrs.pkl', 'rb')

try:
  n_hash = pickle.load(f)
finally:
  f.close()

# this gets the puzzles from puzzle.txt
puzzles_string_arr = open('puzzle.txt').read().split('\n')
puzzles = []
for s in puzzles_string_arr:
  p = s.split()
  if len(p) > 1:
    puzzles.append(p)

# Runs breadth first search between a root (start) and dest (destination)
def bfs(root, dest):
  t1 = time()

  # A FIFO queue is maintained through an array
  q = []

  # The following dictionary has words as keys, and lists of distance, parent as values.
  dist_parent_hash = {}
  for w in n_hash.keys():
    dist_parent_hash[w] = [-1, '']

  dist_parent_hash[root] = [0, '']
  q.append(root)

  count = 0

  max_q_length = 0

  while len(q) > 0:
    if len(q) > max_q_length:
      max_q_length = len(q)
    x = q.pop(0)
    if x == dest:
      break
    count += 1
    neighbors = n_hash[x]
    for n in neighbors:
      if dist_parent_hash[n][0] == -1:
        dist_parent_hash[n][0] = dist_parent_hash[x][0] + 1
        dist_parent_hash[n][1] = x
        q.append(n)

  t2 = time()

  if dist_parent_hash[dest][0] == -1:
    print('The word "' + dest + '" is not connected to the word "' + root + '".')
  else:
    connection = []
    d = dist_parent_hash[dest][0]
    word_to_add = dest
    while d > -1:
      connection.append(word_to_add)
      d -= 1
      word_to_add = dist_parent_hash[word_to_add][1]
    print("The connection between the two words is: ")
    i = len(connection) - 1
    while i > -1:
      print(connection[i])
      i -= 1

    print("The connection is " + str(len(connection) -1) + " edges long.")

  print("It took " + str(t2-t1) + " seconds for the search to run.")
  print("The program cycled through " + str(count) + " words.")
  print("The maximum queue length is " + str(max_q_length) + ".")

for p in puzzles:
  bfs(p[0], p[1])
  print("-----------------------------------------------------------")


