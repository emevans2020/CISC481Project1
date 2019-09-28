# Emily Evans and Sasha Jones			Due: September 28

# List of points that are mapped to each other. 
# Our goal is to get from any point to the goal point, in this case 5

yard = [(1,2),(1,3),(3,5),(4,5),(2,6),(5,6)]  


function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
frontier ← a priority queue ordered by PATH-COST, with node as the only element explored ← an empty set
loop do
if EMPTY?(frontier) then return failure
node←POP(frontier) /*choosesthelowest-costnodeinfrontier */ if problem.GOAL-TEST(node.STATE) then return SOLUTION(node) add node.STATE to explored
for each action in problem.ACTIONS(node.STATE) do
child ←CHILD-NODE(problem,node,action)
if child.STATE is not in explored or frontier then
frontier ←INSERT(child,frontier)
else if child.STATE is in frontier with higher PATH-COST then
replace that frontier node with child

def possible-actions(lst):
	pass
function SIMPLE-PROBLEM-SOLVING-AGENT(percept) returns an action persistent: seq, an action sequence, initially empty
state, some description of the current world state goal, a goal, initially null
problem, a problem formulation
state ← UPDATE-STATE(state,percept) if seq is empty then
goal ← FORMULATE-GOAL(state)
problem ←FORMULATE-PROBLEM(state,goal) seq ← SEARCH(problem)
if seq = failure then return a null action
action ← FIRST(seq) seq ← REST(seq) return action

