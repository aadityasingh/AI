from time import time
import pickle
import Queue
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

q = Queue.Queue()
c = 1

dist_parent_hash = {}
for w in array_of_text_from_file:
  dist_parent_hash[w] = [-1, '']

dist_parent_hash[root] = [0, '']
q.put(root)

while q.empty() == False:
  x = q.get()
  #print(x)
  neighbors = ast.literal_eval(n_hash[x])
  for n in neighbors:
    c += 1
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
  print("The connection is " + str(len(connection)) + " words long, including the start and finish words.")

t2 = time()

print("It took " + str(t2-t1) + " seconds for the search to run.")
print("The program cycled through " + str(c) + " words.")
