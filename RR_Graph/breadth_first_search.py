# This program runs an A* search between two nodes in a graph.

from time import time
import pickle
import sys

network = input('Network of trains (NA or ROM): \n')
if network == 'ROM':
  pickled_file = 'rom_graph.p'
elif network == 'NA':
  pickled_file = 'na_graph.p'
else:
  sys.exit()

f = open(pickled_file, 'rb')

try:
  graph = pickle.load(f)
finally:
  f.close()

root = input('Enter starting word: \n')
dest = input('Enter destination: \n')

t1 = time()

q = []

dist_parent_hash = {}
for w in graph.keys():
  dist_parent_hash[w] = [-1, '', -1]

dist_parent_hash[root] = [0, '', 0]
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

  neighbors = graph[x]
  for node in neighbors:
    n = node[0]
    d = node[1]
    if dist_parent_hash[n][0] == -1:
      dist_parent_hash[n][0] = dist_parent_hash[x][0] + 1
      dist_parent_hash[n][1] = x
      dist_parent_hash[n][2] = dist_parent_hash[x][2] + d
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
  print("The connection is " + str(dist_parent_hash[dest][2]) + " miles long.")

print("It took " + str(t2-t1) + " seconds for the search to run.")
# print("The program cycled through " + str(count) + " words.")