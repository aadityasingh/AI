# This program solves a sudoku with the given configuration.

from time import time

input_file = 'puzzle2.txt'
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

#try making a better measure
# Like if it is a problem in a row and column, count it as 2 errors
def num_of_errors(p, unknowns):
  if len(p) < 2:
    return 1000
  num = 0
  for x in unknowns:
    for n in neighbors_hash[x]:
      if p[x] == p[n]:
        num += 1
        break
  return num


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

def neighbor_positions(p, unknowns):
  retval = {}
  for i in unknowns:
    for j in unknowns[(unknowns.index(i)+1):]:
      next_p = list(p)
      x = next_p[i]
      y = next_p[j]
      next_p[i] = y
      next_p[j] = x
      retval[num_of_errors(next_p, unknowns)] = next_p
  return retval
        

# Only gets to a local min spot
def solve(p, unknowns, count):
  errors = num_of_errors(p, unknowns)
  if errors == 0:
    print("Solved puzzle: ")
    format_print(p)
    print('------------------')
    return True

  if count > 10:
    print("Program reached a local min number of errors of " + str(errors) + ": ")
    format_print(p)
    print('------------------')
    return False

  neighbors = neighbor_positions(p, unknowns)
  min_nbor = neighbors.pop(min(neighbors))

  n_errors = num_of_errors(min_nbor, unknowns)
  if n_errors > errors:
    print("Program reached a local minimum number of errors of " + str(errors) + ": ")
    format_print(p)
    print('------------------')
    return False
  elif n_errors == errors:
    count += 1
    return solve(min_nbor, unknowns, count)
  else:
    count = 0
    return solve(min_nbor, unknowns, count)

# Implements tabu search but is very very slow
def solve2(p, unknowns, maxSize):
  bestp = p
  tabuList = []
  while(num_of_errors(bestp, unknowns) != 0):

    neighbors = neighbor_positions(bestp, unknowns)

    key = min(neighbors)
    min_nbor = neighbors.pop(key)
    while(min_nbor in tabuList):
      key = min(neighbors)
      min_nbor = neighbors.pop(key)

    if key < num_of_errors(bestp, unknowns):
      bestp = min_nbor
    tabuList.append(min_nbor)
    if len(tabuList) > maxSize:
      tabuList.pop(0)

  return bestp


total_poss = []
for i in range(9):
  for j in range(9): total_poss.append(i+1)

for p in puzzles:
  print("Unsolved puzzle #" + str(puzzles.index(p)+1) + ": ")
  format_print(p)
  empty = []
  poss_left = list(total_poss)
  for num in range(81):
    if p[num] == 0:
      empty.append(num)
    else:
      poss_left.remove(p[num])

  if len(empty) == 0:
    if is_solved(p):
      print("Solved puzzle: ")
      format_print(p)
      print('------------------')
      continue
    else:
      print("Puzzle is unsolvable!")
      continue

  if len(empty) != len(poss_left):
    print("Puzzle is unsolvable!!")
    continue

  # Initial "random" assignment
  i = 0
  for n in empty:
    p[n] = poss_left[i]
    i+=1

  #solve(p, empty, 0)
  solvedp = solve2(p, empty, 5)
  print("Solved puzzle: ")
  format_print(solvedp)
  print('------------------')



# t1 = time()
# time_arr = []
# for p in puzzles:
#   tp1 = time()
#   #STUFF
#   tp2 = time()
#   time_arr.append((tp2-tp1))

# t2 = time()

# m1 = max(time_arr)
# i1 = time_arr.index(m1)
# time_arr.remove(m1)
# m2 = max(time_arr)
# i2 = time_arr.index(m2)
# time_arr.remove(m2)
# m3 = max(time_arr)
# i3 = time_arr.index(m3)

# print("The longest puzzle was #" + str(i1+1) + ", and it took " + str(m1) + " seconds.")
# print("The second longest puzzle was #" + str(i2+1) + ", and it took " + str(m2) + " seconds.") 
# print("The third longest puzzle was #" + str(i3+1) + ", and it took " + str(m3) + " seconds.")

# print("The total time to run all of the puzzles is: " + str(t2-t1) + " seconds.")
# # Runs in 11.55 seconds

  


