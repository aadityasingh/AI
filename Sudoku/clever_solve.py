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

def column_list(n):
  # Finds column neighbors
  ret = []
  column = n%9
  for i in range(9):
    if (i*9+column != n):
      ret.append((i*9+column))
  return ret

def row_list(n):
  # Finds row neighbors
  ret = []
  row = n//9
  for i in range(9):
    if (row*9+i != n):
      ret.append((row*9+i))
  return ret

def box_list(n):
  # Finds box neighbors
  ret = []
  b_row = (n//9)//3
  b_column = (n%9)//3
  for i in BOXES[(b_row, b_column)]:
    if i != n:
      ret.append(i)
  return ret

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
  temp_neighbors = column_list(n) + row_list(n) + box_list(n)
  neighbors = list(set(temp_neighbors))

  neighbors_hash[n] = neighbors

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
        return False
      else:
        possible_hash[n] = possible
  return possible_hash
  
#TMP CODE 3

def min_key_by_value(h):
  m = 10
  r = -1
  for i in h:
    if len(h[i]) < m:
      m = len(h[i])
      r = i
  return r

def only_possibles(puz, poss):
  retval = []
  for n in poss:
    for group in [row_list(n), column_list(n), box_list(n)]:
      diff = set(poss[n])
      for nbor in group:
        if puz[nbor] == 0:
          diff = diff - set(poss[nbor])
      if len(diff) == 1:
        t = (n, diff.pop())
        retval.append(t)
        break
      elif len(diff) > 1:
        return False

  return retval

def refresh_possibilities(arr):
  puz = arr[0]
  poss = arr[1]
  if is_solved(puz):
    return [puz, poss]

  x = possibilities(puz)
  if x == False:
    return False

  next_puz = list(puz)
  next_poss = {}

  one_more = False
  for i in x:
    if len(x[i]) == 1:
      next_puz[i] = x[i][0]
      one_more = True
    else:
      next_poss[i] = x[i]

  if one_more:
    return refresh_possibilities([next_puz, next_poss])
  else:
    return [next_puz, next_poss]

def solve(p, h, r_depth):
  if is_valid(p) == False:
    return False
  if is_solved(p):
    print("Solved puzzle: ")
    format_print(p)
    print('------------------')
    return True

  n = min_key_by_value(h)
  for j in h[n]:
    p[n] = j

    x = refresh_possibilities([p, h])
    if x == False:
      continue

    next_p = x[0]
    next_poss_hash = x[1]

    if is_solved(next_p):
      print("Solved puzzle: ")
      format_print(next_p)
      print('------------------')
      return True

    if len(next_poss_hash) == 0:
      if is_solved(next_p):
        print("Solved puzzle: ")
        format_print(next_p)
        print('------------------')
        return True
      else:
        continue

    op_arr = only_possibles(next_p, next_poss_hash)
    if op_arr == False:
      continue

    for t in op_arr:
      next_p[t[0]] = t[1]
      next_poss_hash.pop(t[0])

    if len(next_poss_hash) == 0:
      if is_solved(next_p):
        print("Solved puzzle: ")
        format_print(next_p)
        print('------------------')
        return True
      else:
        continue

    #TMP CODE 4

    #TMP CODE 2

    if solve(next_p, next_poss_hash, (r_depth + 1)):
      return True

  return False

t1 = time()
time_arr = []
for p in puzzles:
  tp1 = time()
  print("Unsolved puzzle #" + str(puzzles.index(p)+1) + ": ")
  format_print(p)
  if is_valid(p) == False:
    print("Puzzle is unsolvable!")
    continue

  x = possibilities(p)
  if x == False:
    print("Puzzle is unsolvable!!")
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
    solve(p, poss_hash, 0)

  tp2 = time()
  time_arr.append((tp2-tp1))

t2 = time()

m1 = max(time_arr)
i1 = time_arr.index(m1)
time_arr.remove(m1)
m2 = max(time_arr)
i2 = time_arr.index(m2)
time_arr.remove(m2)
m3 = max(time_arr)
i3 = time_arr.index(m3)

print("The longest puzzle was #" + str(i1+1) + ", and it took " + str(m1) + " seconds.") # Number 57
print("The second longest puzzle was #" + str(i2+1) + ", and it took " + str(m2) + " seconds.") # Number 79
print("The third longest puzzle was #" + str(i3+1) + ", and it took " + str(m3) + " seconds.") # Number 97

print("The total time to run all of the puzzles is: " + str(t2-t1) + " seconds.")
# Runs in 11.55 seconds

  


