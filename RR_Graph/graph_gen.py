# This program generates the graphs for railroads

# The following names can be changed for a corresponding north american graph.
node_file_name = 'rom_nodes.txt'
edge_file_name = 'rom_edges.txt'
pickle_nodes_file_name = 'rom_node_hash.p'
pickle_graph_file_name = 'rom_graph.p'

from math import pi , acos , sin , cos
import pickle

# Make a node hash, with a name corresponding to a 2-tuple of latitude and longitude
def node_hash():
  h = {}
  array_of_lines_from_file = open(node_file_name).read().split('\n')
  for l in array_of_lines_from_file:
    arr = l.split(' ')
    if len(arr) == 3:
      h[arr[0]] = (float(arr[1]), float(arr[2]))

  return h

n = node_hash()

pickle.dump(n, open(pickle_nodes_file_name, 'wb'))

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
      d = dist(n, arr[0], arr[1])
      g[arr[0]].append((arr[1], d))
      g[arr[1]].append((arr[0], d))

  return g

graph = make_graph(n)

pickle.dump(graph, open(pickle_graph_file_name, 'wb'))
