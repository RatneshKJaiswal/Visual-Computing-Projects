tup = (1,9,5,2,5,3,2,5,2,2)
# tup[0] = 54   -> not possible
print(type(tup),tup)
print(len(tup))
print(tup[2])


res = tup.count(2)
print("Count of 3 is ",res)

# returns first index of 3
res = tup.index(2)
print("Index of 3 is ",res)