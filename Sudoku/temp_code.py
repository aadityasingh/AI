#TMP CODE 1
# x = possibilities(p)
# if x == False:
#   continue

# next_p = list(p)
# next_poss_hash = {}

# for i in x:
#   if len(x[i]) == 1:
#     next_p[i] = x[i][0]
#   else:
#     next_poss_hash[i] = x[i]


#TMP CODE 2
# *** Single possible value code START
# to_pop = []
# cont = False
# for k in next_poss_hash:
#   poss = list(next_poss_hash[k])
#   for c in list(set(column_set(k)) & set(next_poss_hash.keys())):
#     for v in list(set(next_poss_hash[c]) & set(poss)):
#       poss.remove(v)

#   if len(poss) == 1:
#     next_p[k] = poss[0]
#     to_pop.append(k)
#     continue
#   elif len(poss) > 1:
#     cont_val = True

#   poss = list(next_poss_hash[k])
#   for r in list(set(row_set(k)) & set(next_poss_hash.keys())):
#     for v in list(set(next_poss_hash[r]) & set(poss)):
#       poss.remove(v)

#   if len(poss) == 1:
#     next_p[k] = poss[0]
#     to_pop.append(k)
#     continue
#   elif len(poss) > 1:
#     cont_val = True
#     print(str(k) + '-' + s)

#   poss = list(next_poss_hash[k])
#   for b in list(set(box_set(k)) & set(next_poss_hash.keys())):
#     for v in list(set(next_poss_hash[b]) & set(poss)):
#       poss.remove(v)

#   if len(poss) == 1:
#     next_p[k] = poss[0]
#     to_pop.append(k)
#     continue
#   elif len(poss) > 1:
#     cont_val = True      

# if cont:
#   continue

# for tp in to_pop:
#   next_poss_hash.pop(tp)
# *** Single possible value code END