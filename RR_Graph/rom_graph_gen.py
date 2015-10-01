# This program generates the graph for the railroads in Romania.

import math

# Make a node hash, with a name corresponding to a 2-tuple of latitude and longitude
def node_hash():
  h = {}
  array_of_lines_from_file = open('rom_nodes.txt').read().split('\n')
  for l in array_of_lines_from_file:
    arr = l.split()
    h[arr[0]] = (float(arr[1]), float(arr[2]))

  return h

# Finds the distance between two nodes
def dist(n1, n2):
  n = node_hash()
  lat1 = n[n1][0] * math.pi/180
  long1 = n[n1][1] * math.pi/180
  lat2 = n[n2][0] * math.pi/180
  long2 = n[n2][1] * math.pi/180

  del_lat = lat2 - lat1
  del_long = long2 - long1

  # WEBSITE: http://mathforum.org/library/drmath/view/51711.html
  a = math.pow(math.sin(del_lat/2), 2) + math.cos(lat1) * math.cos(lat2) * math.pow(math.sin(del_long/2), 2)


# Makes a hash, where each node corresponds to a list of 2-tuples. Each 2-tuple has the first number referring to another node, and the second number referring to the distance to the node
def make_graph():
  g = {}
  for c in node_hash().keys:
    g[c] = []
  lines_from_file = open('rom_edges.txt').read().split('\n')
  for l in lines_from_file:
    arr = l.split()
    g[arr[0]].append(arr[1])
    g[arr[1]].append(arr[0])

