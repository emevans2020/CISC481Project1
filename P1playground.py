
#Sasha Jones
#September 29th, 2019
#CISC 481
#Program 1 {layground
#Due: Tuesday, October 8th, 2019

#This is just a testing playground for Program 1

print ("Hello World")



def addme ( int1, int2):
    "adds 2 numbers together and prints the result"
    sum = int1 + int2
    print (sum)
    return;

addme(7,3)

Yard3 = [(1,2), (1,3)] # Connections
INIT_STATE_3 = [["*"],["a"],["b"]] #initial state
CurrState = INIT_STATE_3[:]
GOAL_STATE_3 = [["*","a","b"],"",""] #goal state


def inYard (x,y):
    if (x,y) in Yard3:
        return True
    else:
        return False


def LEFT(y,x):
    if (x,y) in Yard3:
        if ("*" in CurrState[x-1] or "*" in CurrState[y-1]):
            return True
        else:
            print (x," and ",  y, " don't have an engine.")
            return False
    else:
        print ("nope")


def TESTleft(y,x):
    print("\t TESTleft \n")

    StOfy = CurrState[y-1].pop(0) #index of the first car on track y
    print("StOfy is :", StOfy)

    CurrState[x-1].append(StOfy)
    print("the Current State now is :\n", CurrState)


def TESTright(x,y):
    print("\t TESTright \n")

    LaOfx = CurrState[x-1].pop() #index of last car on track x
    print("LaOfx is :", LaOfx)

    CurrState[y-1].insert(0,LaOfx)
    print("the Current State now is :\n", CurrState)

print("Initial State 3:\n", INIT_STATE_3)
TESTleft(2,1)
TESTright(1,3)


