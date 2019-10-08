# Emily Evans and Sasha Jones			Due: September 28
#CISC 481
#Programming Assignment 1
# List of points that are mapped to each other. 
# Our goal is to get from any point to the goal point, in this case 5

# Yard1 = [(1,2),(1,3),(3,5),(4,5),(2,6),(5,6)]  dont think about testing yard 1 until you figure out yards 3,4,5

# Yard 3 
Yard3 = [(1,2), (1,3)] # Connections
INIT_STATE_3 = [ ("*"),("a"),("b")] #initial state
CurrState = INIT_STATE_3[:]
GOAL_STATE_3 = [("*","a","b"),"",""] #goal state

Yard4 = [(1,2), (1,3), (1,4)]
Yard5 = [(1,2), (1,3), (1,4)]


# simple problem solving agent
#Consumes a yard and a State and returns a list of all actions possible

def possible_actions (Yard, State):
    actions = []
<<<<<<< HEAD
	
    # for connections in list, see if there 
=======

    # for connections in list, see if there is an engine on either track.
        #If there Is an engine
        #Then see the connections with its neighbors
            #Then see if you can move left and/or right
            # DO NOT include moving on to an empty state
                #ex, moving left from 2 to 1 when there is no car on 2

    
>>>>>>> 2de27a3762109eebe077755468f270b91f1a2c0a

    
    

	return actions

##### TESTING possible_actions

    #possible_actions(Yard3, INIT_STATE_3)

    
########### ACTIONS #######

def left(y,x): # remove last car 
    # if (x,y) is in Yard and x or y contains the engine(*),
    # then remove first car from track y  (list.pop[0])
    #and place at the end of track x (list.append

    StOfy = CurrState[y-1].pop[0] #index of the first car on track y

    CurrState[x-1].append(StOfy)
    print(CurrState)

    return 0

#### TESTING left

#left(2,1) on Yard 3 should result in 


def right(x y):


    return 0


def inYard(Yard, (x,y) ):
    if 

def inYard (x,y):
    if (x,y) in Yard3:
        print ("True")
    else:
        print("False")


#######################

def TESTleft(y,x):

    StOfy = CurrState[y-1].pop(0) #index of the first car on track y
    print("StOfy is :", StOfy)

    CurrState[x-1].append(StOfy)
    print("the Cuurent State now is :\n", CurrState)



def TESTright(x,y):

    LaOfx = CurrState[x-1].pop() #index of last car on track x
    print("LaOfx is :", LaOfx)

    CurrState[y-1].insert(0,LaOfx)
    print("the Current State now is :\n", CurrState)

