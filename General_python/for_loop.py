name = "Ratnesh"
for i in name:
    print(i)
    if(i=='n'):
        print("This is something special")


colour = ["Red","Green","Blue","Yellow"]
for color in colour:
    print(color)
    for i in color:
        print(i)


for k in range(4): # 0 -> 3
    print(k)


for k in range(1,10): # 1 -> 9
    print(k)

# for k in range(x,y,z)     z -> z-1 step skips

for k in range(1,11,3):
    print(k)


# while loop
i=0
while (i<3):
    print(i)
    i=i+1

# using else with while loop
while (i<10):
    print(i)
    i+=1
else:
    print("Ended")