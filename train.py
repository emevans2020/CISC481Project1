# Emily Evans and Sasha Jones			Due: September 28

# List of points that are mapped to each other. 
# Our goal is to get from any point to the goal point, in this case 5

# yard1 = [(1,2),(1,3),(3,5),(4,5),(2,6),(5,6)]  dont think about testing yard 1 until you figure out yards 3,4,5
yard3 = [(1,2), (1,3)]
yard4 = [(1,2), (1,3), (1,4)]
yard5 = [(1,2), (1,3), (1,4)]

# simple problem solving agent
def possible-actions(Yard, State):

	return actions