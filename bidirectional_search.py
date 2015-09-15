from time import time
import pickle
import ast

# this makes an array of all the words in the file
array_of_text_from_file = open('words.txt').read().split()

f = open('save.p', 'rb')

try:
  n_hash = pickle.load(f)
finally:
  f.close()

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

# while len(q_root) != 0:
#   x = q_root.pop(0)
#   neighbors = ast.literal_eval(n_hash[x])
#   for n in neighbors:
#     if dist_parent_hash[n][0] == -1:
#       dist_parent_hash[n][0] = dist_parent_hash[x][0] + 1
#       dist_parent_hash[n][1] = x
#       q_root.append(n)

for r, d in zip(q_root, q_dest):
  n_root = ast.literal_eval(n_hash[r])
  n_dest = ast.literal_eval(n_hash[d])
  for nr in n_root:
    if dist_parent_hash_root[nr][0] == -1:
      dist_parent_hash_root[nr][0] = dist_parent_hash_root[r][0] + 1
      dist_parent_hash_root[nr][1] = r
      q_root.append(nr)
  for nd in n_dest:
    if dist_parent_hash_dest[nd][0] == -1:
      dist_parent_hash_dest[nd[0] = dist_parent_hash_root[d][0] + 1
      dist_parent_hash_dest[nd][1] = d
      q_dest.append(nd)

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
  print("The connection is " + str(len(connection)) + " words long, including the start and finish words.")

t2 = time()

print("It took " + str(t2-t1) + " seconds for the search to run.")
print("The program cycled through " + str(c) + " words.")
