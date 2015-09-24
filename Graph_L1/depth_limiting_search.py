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

root = input('Enter starting word: \n')
dest = input('Enter destination: \n')

t1 = time()

dist_parent_hash = {}
for w in array_of_text_from_file:
  dist_parent_hash[w] = [-1, '']

# while len(stack) > 0:
#   x = stack.pop()
#   neighbors = ast.literal_eval(n_hash[x])
#   if dist_parent_hash[x][0] < level:
#     for n in neighbors:
#       count += 1
#       if dist_parent_hash[n][0] == -1:
#         dist_parent_hash[n][0] = dist_parent_hash[x][0] + 1
#         dist_parent_hash[n][1] = x
#         stack.append(n)
#   else:
#     stack.append(x)

# def dls(node, problem, limit):
#   if dist_parent_hash[problem][0] != -1:
#     return True
#   elif dist_parent_hash[node][0] == limit:
#     return 'cutoff'
#   else:
#     neighbors = ast.literal_eval(n_hash[x])
#     for n in neighbors:
#       if dist_parent_hash[n][0] == -1:
#         dist_parent_hash[n][0] = dist_parent_hash[x][0] + 1
#         dist_parent_hash[n][1] = x
#         stack.append(n)

def dls(node, problem, parent, limit):
  if parent == '':
    distance = 0
  else:
    distance = dist_parent_hash[parent][0] + 1

  if distance < limit:
    if dist_parent_hash[node][0] == -1:
      dist_parent_hash[node][1] = parent
      dist_parent_hash[node][0] = distance

      if node == problem:
        return 100
      else:
        neighbors = ast.literal_eval(n_hash[node])
        retval = 1
        for n in neighbors:
          r = dls(n, problem, node, limit)
          if r > retval:
            retval = r

        return retval
    else:
      return 1
  else:
    return 2

lim = 0
inc_limit = dls(root, dest, '', lim)
while inc_limit == 2:
  for w in dist_parent_hash.keys():
    dist_parent_hash[w] = [-1, '']
  lim += 1
  inc_limit = dls(root, dest, '', lim)


found_word = inc_limit

if found_word == 1:
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

t2 = time()

print("It took " + str(t2-t1) + " seconds for the search to run.")
# print("The program cycled through " + str(count) + " words.")