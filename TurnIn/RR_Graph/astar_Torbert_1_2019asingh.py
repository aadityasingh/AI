# This program runs an A* search between two nodes in a railroad network.

from math import pi , acos , sin , cos

# The following names can be changed for a corresponding north american graph.
node_file_name = 'nodes.txt'
edge_file_name = 'edges.txt'

# Make a node hash, with a name corresponding to a 2-tuple of latitude and longitude
def node_hash():
  h = {}
  array_of_lines_from_file = open(node_file_name).read().split('\n')
  for l in array_of_lines_from_file:
    arr = l.split(' ')
    if len(arr) == 3:
      h[arr[0]] = (float(arr[1]), float(arr[2]))

  return h

nodes = node_hash()

# Finds the distance between two cities which are keys in the hash n
def dist(n, n1, n2):
  lat1 = n[n1][0] * pi/180.0
  long1 = n[n1][1] * pi/180.0
  lat2 = n[n2][0] * pi/180.0
  long2 = n[n2][1] * pi/180

  R   = 3958.76

  return acos( sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(long2-long1) ) * R

# Makes a hash, where each node corresponds to a list of 2-tuples. Each 2-tuple has the first number referring to another node, and the second number referring to the distance to the node
def make_graph(n):
  g = {}
  for c in n.keys():
    g[c] = []
  lines_from_file = open(edge_file_name).read().split('\n')
  for l in lines_from_file:
    arr = l.split()
    if len(arr) == 2:
      d = dist(nodes, arr[0], arr[1])
      g[arr[0]].append((arr[1], d))
      g[arr[1]].append((arr[0], d))

  return g

graph = make_graph(nodes)

def search(root, dest):
  dist_parent_hash = {}
  for w in graph.keys():
    dist_parent_hash[w] = [-1, '', -1]

  dist_parent_hash[root] = [0, '', 0]

  d_root = dist(nodes, root, dest)
  q = {d_root: root}

  closed_set = []

  while len(q) > 0:
    x = q.pop(min(q))

    if x == dest:
      break

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
        q[(dist_parent_hash[n][2] + dist(nodes, n, dest))] = n

  if dist_parent_hash[dest][0] == -1:
    print('The node "' + dest + '" is not connected to the node "' + root + '".')
  else:
    print("The connection is " + str(dist_parent_hash[dest][2]) + " miles long.")

  print("The size of the closed set is " + str(len(closed_set)) + ".")

puzzles = open('puzzle.txt').read().split('\n')
for p in puzzles:
  p_arr = p.split()
  if len(p_arr) > 1:
    print("For the nodes " + p_arr[0] + " and " + p_arr[1] + ":")
    search(p_arr[0], p_arr[1])
    print("------------------------------------------------------------------------")