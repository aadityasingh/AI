# This program runs an A* search between two nodes in a railroad network.

from time import time
import pickle
import sys
from math import pi , acos , sin , cos

network = input('Network of trains (NA or ROM): \n')
if network == 'ROM':
  pickled_nodes_file = 'rom_node_hash.p'
  pickled_graph_file = 'rom_graph.p'
elif network == 'NA':
  pickled_graph_file = 'na_graph.p'
  pickled_nodes_file = 'na_node_hash.p'
else:
  sys.exit()

f_node = open(pickled_nodes_file, 'rb')

try:
  nodes = pickle.load(f_node)
finally:
  f_node.close()

f = open(pickled_graph_file, 'rb')

try:
  graph = pickle.load(f)
finally:
  f.close()

root = input('Enter starting city: \n')
dest = input('Enter destination: \n')

def dist_to_dest(n):
  lat1 = nodes[n][0] * pi/180.0
  long1 = nodes[n][1] * pi/180.0
  lat2 = nodes[dest][0] * pi/180.0
  long2 = nodes[dest][1] * pi/180

  R   = 3958.76

  return acos( sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(long2-long1) ) * R


t1 = time()

dist_parent_hash = {}
for w in graph.keys():
  dist_parent_hash[w] = [-1, '', -1]

dist_parent_hash[root] = [0, '', 0]

d_root = 0 #dist_to_dest(root)
q = {d_root: root}

count = 0

max_q_length = len(q)

closed_set = []

while len(q) > 0:
  if len(q) > max_q_length:
    max_q_length = len(q)

  x = q.pop(min(q))

  if x == dest:
    break
  count += 1

  # The following is used to calculate closed set size
  # It increases runtime significantly!
  if (x in closed_set) == False:
    closed_set.append(x)

  neighbors = graph[x]
  for node in neighbors:
    n = node[0]
    d = node[1]
    distance = dist_parent_hash[x][2] + d
    if ( (dist_parent_hash[n][0] == -1) | (dist_parent_hash[n][2] > distance) ):
      dist_parent_hash[n][0] = dist_parent_hash[x][0] + 1
      dist_parent_hash[n][1] = x
      dist_parent_hash[n][2] = distance
      q[(dist_parent_hash[n][2] + 0)] = n # dist_to_dest(n)


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
print("The search cycled through " + str(count) + " cities.")
print("The size of the closed set is " + str(len(closed_set)) + ".")
print("The maximum queue length was " + str(max_q_length) + ".")