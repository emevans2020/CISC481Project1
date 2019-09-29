# Emily Evans and Sasha Jones			Due: October 1

# List of points that are mapped to each other. 
# Our goal is to get from any point to the goal point, in this case 5

# yard1 = [(1,2),(1,3),(3,5),(4,5),(2,6),(5,6)]  dont think about testing yard 1 until you figure out yards 3,4,5
yard3 = [(1,2), (1,3)]
yard4 = [(1,2), (1,3), (1,4)]
yard5 = [(1,2), (1,3), (1,4)]

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

# percept - agent's perceptual inputs at any given instance. An agent's percept sequence is the complete
# history of everything the agent has ever perceived
# simple problem solving agent
def possible-actions(Yard, State):
	
	return actions