# Emily Evans and Sasha Jones			Due: October 1
# List of points that are mapped to each other. 
# Our goal is to get from any point to the goal point, in this case 5

# yard1 = [(1,2),(1,3),(3,5),(4,5),(2,6),(5,6)]  dont think about testing yard 1 until you figure out yards 3,4,5
yard3 = [(1,2), (1,3)]
yard4 = [(1,2), (1,3), (1,4)]
yard5 = [(1,2), (1,3), (1,4)]

#  for possible-actions you just need to say usin ex yard 1:
# ["right", 1,2] or ["right", 1,3] and list out possible options
# Don't need to do error checking

# here are the initial states 
initState1 = ['*','e','','bca','','d']
initState3 = ['*','a','b']
initState4 = ['*','a','bc','d']
initState5 = ['*','a', 'c b','d']

# listed below are the goal states for the yard
goalState3 = ['* a b','','']
goalState4 = ['* a b c d','','','']
goalState5 = ['* a b c d','','','']

# dictionary version of the yards below
yardOne = {	"1": ["2","3"],
			"2": ["1","6"],
			"3": ["1","5"],
			"4": ["5"],
			"5": ["6","4"],
			"6": ["5","2"]
}
yardTwo = {	"1": ["2","5"],
			"2": ["3","4"],
			"3": ["2"],
			"4": ["2"],
			"5": ["1"]
}
yardThree = {"1": ["2","3"], 
			"2": ["1"],
			"3":["1"]
}
yardFour = {"1": ["2","3","4"],
			"2": ["1"],
			"3": ["1"],
			"4": ["1"]
}

yardFive = {"1": ["2","3","4"],
			"2": ["1"],
			"3": ["1"],
			"4": ["1"]
}
# make function called contains to check if * is contained -- have boolean return value
def contains (Yard, State):
	for (i in State){
		if (i == "*"){
			return true
		}
	}
	else{
		return false
	}

# percept - agent's perceptual inputs at any given instance. An agent's percept sequence is the complete
# history of everything the agent has ever perceived
# simple problem solving agent
def possible-actions(Yard):
	initState = State
	return actions

def left (x,y):
	if (contains == true){
		#do something
	}
	else if{
	}
	
	
