#TMP Code 1
# errors = num_of_errors(p, unknowns)
# f = depth + errors

# if (errors == 0):
#   print("Solved puzzle: ")
#   format_print(next_p)
#   print('------------------')
#   return True

# dist_hash = {}
# for n_pos in neighbor_positions(p, unknowns):
#   n_errors = num_of_errors(n_pos, unknowns)
#   n_f = depth + 1 + errors
#   dist_hash[n_f] = n_pos

# while len(dist_hash) > 0:
#   next_p = dist_hash.pop(min(dist_hash))
#   recur_val = solve(next_p, unknowns, (depth+1))
#   if recur_val: return True