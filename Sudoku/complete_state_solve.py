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

def num_of_errors(p, unknowns):
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

def solve(p, unknown, poss):
  if (num_of_errors(p) == 0):
    print("Solved puzzle: ")
    format_print(next_p)
    print('------------------')
    return True


total_poss = []
for i in range(9):
  for j in range(9): total_poss.append(i)

for p in puzzles:
  empty = []
  poss_left = list(total_poss)
  for num in p:
    if p[num] == 0:
      empty.append(num)
    else:
      poss_left.remove(p[num])

  if len(empty) == 0:
    if is_solved(p):
      print("Solved puzzle: ")
      format_print(next_p)
      print('------------------')
      continue
    else:
      print("Puzzle is unsolvable!!!")
      continue

  if len(empty) != len(poss_left):
    print("Puzzle is unsolvable!!!")
    continue

  

  solve(p, empty, poss_left)



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

  


