def calculateGM(a,b):
    mean = (a*b)/(a+b)
    return mean

def isGreater(a,b):
    pass    # baad mai likhunga 

x=10
y=20
print(calculateGM(x,y))


# To pass a tuple , use ** for dictionary
def findAvg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is ",sum/len(numbers))

findAvg(19,43)