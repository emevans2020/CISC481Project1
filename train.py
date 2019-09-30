# Emily Evans and Sasha Jones			Due: October 1

# List of points that are mapped to each other. 
# Our goal is to get from any point to the goal point, in this case 5

# Yard1 = [(1,2),(1,3),(3,5),(4,5),(2,6),(5,6)]  dont think about testing yard 1 until you figure out yards 3,4,5

# Yard 3 
Yard3 = [(1,2), (1,3)] # Connections
INIT_STATE_3 = [ ("*"),("a"),("b")] #initial state
GOAL_STATE_3 = [("*","a","b"),"",""] #goal state

Yard4 = [(1,2), (1,3), (1,4)]
Yard5 = [(1,2), (1,3), (1,4)]

print ("Hello World")

# dictionary version of the yards below
yardOne = {	"1": ["2","3"],
			"2": ["6"],
			"3": ["5"],
			"4": ["5"],
			"5": ["6"],
			"6": []
}
yardThree = {"1": ["2","3"], 
			"2": [],
			"3":[]
}
yardFour = {"1": ["2","3","4"],
			"2": [],
			"3": [],
			"4": []
}

yardFive = {"1": ["2","3","4"],
			"2": [],
			"3": [],
			"4": []
}
# make function called contains to check if * is contained -- have boolean return value

# percept - agent's perceptual inputs at any given instance. An agent's percept sequence is the complete
# history of everything the agent has ever perceived
# simple problem solving agent
<<<<<<< HEAD
#Consumes a yard and a State and returns a list of all actions possible

def possible_actions (Yard, State):

    actions = []

    # for connections in list, see if there 

    
    

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






=======
def possible-actions(Yard, State):
	
	return actions

def left (x,y):
	if (contains == true){
		#do something
	}
	else if{
	}
	
	
>>>>>>> abbe286e18732672f262a7e13857c1d68c740807
