def main():
	"""
	All of the sequential code that is necesary to run this application  is located here
	TODO: figure out global variables (if necessary), figure out sequential logic
	"""
	print('Do things here')

def find_contours():
	"""
	All of the logic that is needed for finding the contours is located here.
	TODO: add parameters, add logic, add return
	"""
	print('Contours found!')

def find_avg_color():
	"""
	All of the logic that is needed for finding the average color inside a contour is located here
	TODO: add parameters, add logic, add return
	"""
	print('Avg color found')

def assign_resource():
	"""
	All logic that is needed for assigning resources to a tile in the list of contours
	TODO: figure out if this function is necessary, this could be abosrbed into find_avg_color()
	"""
	print('Resouces found')

def find_pip_tokens():
	"""
	Locate pip tiles, read values, and associate them with board tiles
	TODO: figure out if this can all be one function or if it needs to be broken up
	"""

def find_settlments():
	"""
	Locate settlements for each color on the board, assign them to the color that they belong to
	TODO: figure out if this can be combined with find roads
	"""

def find_roads():
	"""
	Locate roads for each color on the board, assign them to the color they belong to
	TODO: figure out if this can be combined with find settlements
	"""

def calc_VP():
	"""
	Calculate the victory points for each player. Identify the winner (assuming no one has: Largest road, Largest army, or VP cards)
	TODO: add logic and parameters
	"""

##############################################################################
# THE STRECH GOAL FUNCTIONS ARE BELOW, THEY WILL REMAIN EMPTY AND BELOW THIS
# DO NOT ATTEMPT IMPLEMENTATION OF THESE FUNCTIONS UNLESS WE FIND THEY ARE
# NECESSARY OR WE HAVE ACHIEVED THE ABOVE FUNCTIONS
##############################################################################

# Function associated with handling player hands, this would assume that all players would play open handed

# Function associated with finding the longest road

# ALL functions associated with handling game assistant or AI implementation

if __name__ == '__main__':
	main()
