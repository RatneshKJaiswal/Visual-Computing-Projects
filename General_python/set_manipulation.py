s1={1,2,3,5}
s2={3,5,6}

print(s1.union(s2))
print(s1.intersection(s2))

# s1.update(s2)     this update s1 into s1 U s2

print(s1.symmetric_difference(s2))      # prints non common elements  AUB - A^B

print(s1.difference(s2))   # A-B

print(s1.isdisjoint(s2))   # disjoint - no elements in common

print(s1.issuperset(s2))   # is s1 superset of s2
print(s1.issubset(s2))

s1.add(8)
s1.remove(1)
print(s1)

item = s1.pop()
print(s1)
print(item)

s3={3,5,1,8}
print(s3)
s3.clear()
print(s3)

if 4 in s1:
    print("yes")
else:
    print("No")
