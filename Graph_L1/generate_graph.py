# Uses python 2

from time import time
import pickle
import ast

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
    h[str(word)] = all_neighbors_for_word(word)
  return h

print("Making graph...")
t1 = time()
n_hash = neighbors_hash()
t2 = time()
print("Finished making graph! Took " + str(t2-t1) + " seconds to complete")

pickle.dump(n_hash, open('saved_graph.p', 'wb'))