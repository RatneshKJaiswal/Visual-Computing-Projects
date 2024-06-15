marks = [3,2,6,4,1,80,22,12,54,62]
print(marks)
print(type(marks))
print(marks[2])

#  sliced 1->5 print with 2-1=1 jumps
print(marks[1:6:2])

lst = [i*i for i in range(4)]
print(lst)

l = [41,75,3,1,9,32,66,41,99]
print(l)
l[1] = 91
print(l)
l.insert(2,41)
print(l)
m = [21,65,23]
l.extend(m)
print(l)