# Works in python 2
# Python 3 implementation is not finished
# because zip works differently in Python 3.

from time import time
import pickle

# this makes an array of all the words in the file
array_of_text_from_file = open('words.txt').read().split()

f = open('saved_graph.p', 'rb')

try:
  n_hash = pickle.load(f)
finally:
  f.close()

#Makes a nice array of a connection
def connection(h, w):
  connection = []
  d = h[w][0]
  word_to_add = w
  while d > -1:
    connection.append(word_to_add)
    d -= 1
    word_to_add = h[word_to_add][1]
  return connection

root = raw_input('Enter starting word: \n')
dest = raw_input('Enter destination: \n')

t1 = time()

q_root = []
q_dest = []

dist_parent_hash_root = {}
dist_parent_hash_dest = {}
for w in array_of_text_from_file:
  dist_parent_hash_dest[w] = [-1, '']
  dist_parent_hash_root[w] = [-1, '']

dist_parent_hash_root[root] = [0, '']
dist_parent_hash_dest[dest] = [0, '']
q_root.append(root)
q_dest.append(dest)

root_side = ''
dest_side = ''
middle = ''

i = 0
pairs = zip(q_root, q_dest)
l = len(pairs)
count = 0

while i < l:
  r = pairs[i][0]
  d = pairs[i][1]
  n_root = n_hash[r]
  for nr in n_root:
    if dist_parent_hash_root[nr][0] == -1:
      count += 1
      dist_parent_hash_root[nr][0] = dist_parent_hash_root[r][0] + 1
      dist_parent_hash_root[nr][1] = r
      q_root.append(nr)

  n_dest = n_hash[d]
  for nd in n_dest:
    if dist_parent_hash_dest[nd][0] == -1:
      count += 1
      dist_parent_hash_dest[nd][0] = dist_parent_hash_dest[d][0] + 1
      dist_parent_hash_dest[nd][1] = d
      q_dest.append(nd)
  
  intersection = set(q_root)&set(q_dest)
  if len(intersection) > 0:
    middle = intersection.pop()
    root_side = r
    dest_side = d
    break

  i += 1
  pairs = zip(q_root, q_dest)
  l = len(pairs)

if middle == '':
  print('The word "' + dest + '" is not connected to the word "' + root + '".')
else:
  root_connection = connection(dist_parent_hash_root, root_side)
  dest_connection = connection(dist_parent_hash_dest, dest_side)
  print("The connection between the two words is: ")
  i = len(root_connection) - 1
  while i > -1:
    print(root_connection[i])
    i -= 1
  print(middle)
  i = 0
  while i < len(dest_connection):
    print(dest_connection[i])
    i += 1

  print("The connection is " + str(len(root_connection) + len(dest_connection)) + " edges long.")



# if dist_parent_hash[dest][0] == -1:
#   print('The word "' + dest + '" is not connected to the word "' + root + '".')
# else:
#   connection = []
#   d = dist_parent_hash[dest][0]
#   word_to_add = dest
#   while d > -1:
#     connection.append(word_to_add)
#     d -= 1
#     word_to_add = dist_parent_hash[word_to_add][1]
#   print("The connection between the two words is: ")
#   i = len(connection) - 1
#   while i > -1:
#     print(connection[i])
#     i -= 1
#   print("The connection is " + str(len(connection)) + " words long, including the start and finish words.")

t2 = time()

print("It took " + str(t2-t1) + " seconds for the search to run.")
print("The search cycled through " + str(count) + " words.")
# print("The program cycled through " + str(c) + " words.")
