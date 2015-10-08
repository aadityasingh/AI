# This program solves an n-puzzle

# Takes in square size and initial configuration
square_size = input("Please input the side length of the square: \n")
print("Please enter the numbers in the square in the following way (example below): ")
print("If you wanted to enter the following configuration for a side length of 3, ")
print("7 2 4")
print("5   6")
print("8 3 1")
print("then you would type in '7 2 4 5 0 6 8 3 1'")
print("Note that the blank spot is represented by the number 0.")
num_string = input("Now, input the properly formatted string for your configuration: \n")

square = []
for i in num_string.split():
  square.append(int(i))

DISTANCE_HASH  = {}
for i in range(9):
  for j in range(i, 9):
    DISTANCE_HASH[(i, j)] = j - i
    DISTANCE_HASH[(j, i)] = j - i

# Modify distance hash for exceptions
DISTANCE_HASH[(1, 4)] = 1
DISTANCE_HASH[(2, 5)] = 1
DISTANCE_HASH[(1, 4)] = 1
DISTANCE_HASH[(1, 4)] = 1
DISTANCE_HASH[(1, 4)] = 1
DISTANCE_HASH[(1, 4)] = 1
DISTANCE_HASH[(1, 4)] = 1
DISTANCE_HASH[(1, 4)] = 1
DISTANCE_HASH[(1, 4)] = 1

def dist_to_dest(num, square_config):


def heuristic(square_config):
