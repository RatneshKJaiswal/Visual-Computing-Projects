x=2
match x:
    case 0:
        print("x is 0")
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case _ if x!=4:
        print("default")
    case _ if x==4:
        print("FBI")

