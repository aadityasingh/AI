from time import time
import pickle
import Queue
import ast

tic = time()

# this makes an array of all the words in the file
array_of_text_from_file = open('words.txt').read().split()

# This method checks if two words are neighbors
def isNeighbor(w1, w2):
  n = len(w1)
  if (n != len(w2)):
    return False

  numDiff = 0
  for i in range(n):
    if (w1[i] != w2[i]):
      numDiff += 1

  if (numDiff == 1):
    return True
  else:
    return False

# This method gets all the neighbors of a certain word
def all_neighbors_for_word(w):
  neighbors = []
  for other_word in array_of_text_from_file :
    if isNeighbor(w, other_word):
      neighbors.append(other_word)

  return neighbors

# Generates a hash where each word is a key and its value is an array of neighbors
def neighbors_hash():
  h = {}
  for word in array_of_text_from_file:
    h[str(word)] = str(all_neighbors_for_word(word))
  return h

# Takes a word as input, and prints out its neighbors
word = raw_input('Enter word to find neighbors for: \n')
n = all_neighbors_for_word(word)
print('There are ' + str(len(n)) + ' neighbors:')
print('\n'.join(n))

# print("Making graph...")
# t1 = time()
# n_hash = neighbors_hash()
# t2 = time()
# print("Finished making graph! Took " + str(t2-t1) + " seconds to complete")

f = open('save.p', 'rb')

try:
  n_hash = pickle.load(f)
finally:
  f.close()


# # Prints out the neigbors' neighbors of the word taken in earlier
# for w in n:
#   n2 = n_hash[w]
#   print('There are ' + str(len(n2)) + ' neighbors for "' + w + '":')
#   print('\n'.join(n2))

# # Prints out the three words with the most neighbors
# print("Identify three words with the most neighbors")
# t3 = time()
# sorted_val_array = sorted(n_hash.values(), key=len, reverse=True)
# t4 = time()
# inv_neighbors_hash = {v: k for k, v in n_hash.items()}
# most_neighbors = inv_neighbors_hash[sorted_val_array[0]]
# print('The word with the most neighbors is: ' + most_neighbors + ". It has " + str(len(sorted_val_array[0])/10) + " neighbors.")
# print("It's neighbors are " + n_hash[most_neighbors])
# second_most_neighbors = inv_neighbors_hash[sorted_val_array[1]]
# print('The word with the second most neighbors is: ' + second_most_neighbors + ". It has " + str(len(sorted_val_array[1])/10) + " neighbors.")
# print("It's neighbors are " + n_hash[second_most_neighbors])
# third_most_neighbors = inv_neighbors_hash[sorted_val_array[2]]
# print('The word with the third most neighbors is: ' + third_most_neighbors + ". It has " + str(len(sorted_val_array[2])/10) + " neighbors.")
# print("It's neighbors are " + n_hash[third_most_neighbors])
# print("Finished identifying! Took " + str(t4-t3) + " seconds to complete")


# #Prints out the degree and frequency
# l = 140
# deg_array = [0] * 15
# n = 0
# for arr in sorted_val_array:
#   if len(arr) == l:
#     deg_array[n] += 1
#   else:
#     n += 1
#     l -= 10
#     if n < 15:
#       deg_array[n] += 1

# deg_array[14] = len(array_of_text_from_file) + 1 - sum(deg_array)

# n = 14
# for num in deg_array:
#   print("The number of words with degree " + str(n) + " is " + str(num))
#   n -=1

# Finds the shortest path between two words in the graph
root = raw_input('Enter starting word: \n')
dest = raw_input('Enter destination: \n')

t1 = time()

q = Queue.Queue()

dist_parent_hash = {}
for w in array_of_text_from_file:
  dist_parent_hash[w] = [-1, '']

dist_parent_hash[root] = [0, '']
q.put(root)

count = 0

while q.empty() == False:
  x = q.get()
  if x == dest:
    break
  count += 1
  neighbors = ast.literal_eval(n_hash[x])
  for n in neighbors:
    if dist_parent_hash[n][0] == -1:
      dist_parent_hash[n][0] = dist_parent_hash[x][0] + 1
      dist_parent_hash[n][1] = x
      q.put(n)

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

t2 = time()

print("It took " + str(t2-t1) + " seconds for the search to run.")
print("The program cycled through " + str(count) + " words.")

toc = time()

print("Program ran in " + str(toc - tic) + " seconds")
