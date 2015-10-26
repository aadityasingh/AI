# This program solves a sudoku with the given configuration.

from time import time

input_file = 'puzzle.txt'
BOXES = {}
BOXES[(0, 0)] = [0, 1, 2, 9, 10, 11, 18, 19, 20]
BOXES[(0, 1)] = [3, 4, 5, 12, 13, 14, 21, 22, 23]
BOXES[(0, 2)] = [6, 7, 8, 15, 16, 17, 24, 25, 26]
BOXES[(1, 0)] = [27, 28, 29, 36, 37, 38, 45, 46, 47]
BOXES[(1, 1)] = [30, 31, 32, 39, 40, 41, 48, 49, 50]
BOXES[(1, 2)] = [33, 34, 35, 42, 43, 44, 51, 52, 53]
BOXES[(2, 0)] = [54, 55, 56, 63, 64, 65, 72, 73, 74]
BOXES[(2, 1)] = [57, 58, 59, 66, 67, 68, 75, 76, 77]
BOXES[(2, 2)] = [60, 61, 62, 69, 70, 71, 78, 79, 80]

puzzle_strings = open(input_file).read().split('\n')

puzzles = []
for s in puzzle_strings:
  if len(s) > 2:
    p = []
    for c in s:
      if c == '.':
        p.append(0)
      else:
        p.append(int(c))
    
    puzzles.append(p)

# Make the hash of neighbors
neighbors_hash = {}
for n in range(81):
  neighbors = []

  # Add column neighbors
  column = n%9
  for i in range(9):
    if (i*9+column != n):
      neighbors.append((i*9+column))

  # Add row neighbors
  row = n//9
  for i in range(9):
    if (row*9+i != n):
      neighbors.append((row*9+i))

  # Add box neighbors
  b_row = row//3
  b_column = column//3
  for i in BOXES[(b_row, b_column)]:
    if ((i != n) & ((i in neighbors) == False)):
      neighbors.append(i)

  neighbors_hash[n] = neighbors

# *** IS VALID IS NOT WORKING!!!
def is_valid(p):
  for n in range(81):
    for i in neighbors_hash[n]:
      if p[i] != 0:
        if p[n] == p[i]:
          return False

  return True

def is_solved(p):
  if 0 in p:
    return False
  else:
    return is_valid(p)

def format_print(p):
  for i in range(9):
    line = ''
    for j in range(9):
      x = p[i*9+j]
      if x == 0:
        line += '  '
      else:
        line += str(p[i*9+j]) + ' '

    print(line)

def possibilities(p):
  possible_hash = {}
  for n in range(81):
    if p[n] == 0:
      possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      for i in neighbors_hash[n]:
        if p[i] in possible:
          possible.remove(p[i])

      if len(possible) == 0:
        print("Puzzle is unsolvable!!")
        return False
      else:
        possible_hash[n] = possible
  return possible_hash

def min_key_by_value(h):
  m = 10
  r = -1
  for i in h:
    if len(h[i]) < m:
      m = len(h[i])
      r = i
  return r

def solve(p, h):
  if is_valid(p) == False:
    return False
  if is_solved(p):
    print("Solved puzzle: ")
    format_print(p)
    print('------------------')
    return True

  # n = p.index(0)
  # for i in range(9):
  #   p[n] = i+1
  #   if solve(list(p)):
  #     return True

  # return False
  n = min_key_by_value(poss_hash)
  for j in poss_hash[n]:
    p[n] = j

    x = possibilities(p)
    if x == False:
      continue

    next_poss_hash = {}
    for i in x:
      if len(x[i]) == 1:
        p[i] = x[i][0]
      else:
        next_poss_hash[i] = x[i]

    if len(next_poss_hash) == 0:
      print("Solved puzzle: ")
      format_print(p)
      print('------------------')
      return True
    
    if solve(list(p), next_poss_hash):
      return True

  return False


for p in puzzles:
  print("Unsolved puzzle #" + str(puzzles.index(p)) + ": ")
  format_print(p)
  if is_valid(p) == False:
    print("Puzzle is unsolvable!")
    continue

  x = possibilities(p)
  if x == False:
    continue

  poss_hash = {}
  for i in x:
    if len(x[i]) == 1:
      p[i] = x[i][0]
    else:
      poss_hash[i] = x[i]

  if len(poss_hash) == 0:
    print("Solved puzzle: ")
    format_print(p)
    print('------------------')
  else:
    solve(p, poss_hash)
    

  


