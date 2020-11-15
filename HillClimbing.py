import random
from pprint import pprint
import time
iterations = 200

def HillClimbing(board, n, max_iterations=200, verbose=False):
	''' Steepest Hill climbing without sideways move, returns the current steps and whether the run succeeded or not '''
	steps = 0
	success = False
	current_board = board.copy()

	if (verbose):
		printBoard(current_board, n)
	
	# Until maximum iterations are reached, search for a solution
	for i in range(max_iterations):
		# Get the least heuristic child from the find child helper function
		next_node = find_child(current_board, n).copy()
		if (verbose and len(next_node) != 0):
			printBoard(next_node, n)
		# Update the steps taken for this run
		steps += 1
		# If we have a child and its heuristic cost is zero, we have a solution
		if (len(next_node) != 0) and (heuristicCost(next_node, n) == 0):
			success = True
			break
		# If we do not get a child, we cannot get a solution
		if (len(next_node) == 0):
			break
		# Make the current child the next node
		current_board = next_node.copy()
	return steps, success

def printBoard(board, n):
	''' Helper function for printing board '''
	print('Board:')
	for i in range(len(board)):
		print(str(board[i]) + ' ', end='')
		if (i + 1) % n == 0:
			print()
	print('H value: ', heuristicCost(board, n))
	print('---------------------')

def generateRandomBoard(n):
	''' Generates a random board for initialization, queens have been calculated row-wise '''
	generated_board = []
	for i in range(n):
		j = random.randint(0, n-1)
		row = [0]*n
		row[j] = 1
		generated_board.extend(row)
	return generated_board

def find_collisions(board, n):
	''' Helper function for calculating queen position collisions '''
	collisions = 0
	occurences = []
	max_index = len(board)
	for i in range(max_index):
		# For each queen on the board, count collisions with other queens, and which kind of collisions they are
		if board[i] == 1:
			for x in range(1, n):
				# checking above current index
				if (i - n*x >= 0):
					north = i - n*x
					# direction north
					if (board[north] == 1):
						collisions += 1
						occurences.append('north: '+str(i)+' and '+str(north))
					# direction northeast
					if (int((north + x)/n) == int(north/n)):
						northeast = north + x
						if (board[northeast] == 1):
							collisions += 1
							occurences.append('northeast: '+str(i)+' and '+str(northeast))
					# direction northwest
					if (int((north - x)/n) == int(north/n)) and (north - x) >= 0:
						northwest = north - x
						if (board[northwest] == 1):
							collisions += 1
							occurences.append('northwest: '+str(i)+' and '+str(northwest))
				# checking below current index
				if (i + n*x < max_index):
					south = i + n*x
					# direction south
					if (board[south] == 1):
						collisions += 1
						occurences.append('south: '+str(i)+' and '+str(south))
					# direction southeast
					if (int((south + x)/n) == int(south/n)) and ((south + x) < max_index):
						southeast = south + x
						if (board[southeast] == 1):
							collisions += 1
							occurences.append('southeast: '+str(i)+' and '+str(southeast))
					# direction southwest
					if (int((south - x)/n) == int(south/n)):
						southwest = south - x
						if (board[southwest] == 1):
							collisions += 1
							occurences.append('southwest: '+str(i)+' and '+str(southwest))
				# direction east (for completeness)
				if (int((i + x)/n) == int(i/n)) and (i + x < max_index):
					east = i + x
					if (board[east] == 1):
						collisions += 1
						occurences.append('east: '+str(i)+' and '+str(east))
				# direction west (for completeness)
				if (int((i - x)/n) == int(i/n)) and (i - x >= 0):
					west = i - x
					if (board[west] == 1):
						collisions += 1
						occurences.append('west: '+str(i)+' and '+str(west))

	return [collisions, occurences]

def heuristicCost(board, n, verbose=False):
	''' Function to determine heuristic - total collisions on the board '''
	collisions, occurences = find_collisions(board, n)
	if verbose:
		pprint(occurences)
	# return half the collisions, since each colliding position is counted twice from the helper function
	return int(collisions/2)

def find_child(board, n, sideways_move=False):
	#This function is used to find that successor whose heuristic value is less than that of the heuristic value of the board currently
	child = []
	#currHeuristicCost gives the heuristic cost of the current state of the board
	currHeuristicCost = heuristicCost(board, n)
	same_cost_children = []

	for row in range(n):
		for col in range(n):
			# Build a temporary board which changes the position of the queen in the current board
			temp = []
			temp.extend(board[:row*n])
			new_row = [0]*n
			new_row[col] = 1
			temp.extend(new_row)
			temp.extend(board[(row+1)*n:])
			temp_h_cost = heuristicCost(temp, n)
			if (sideways_move):
				# if sideways moves are allowed, and the generated child heuristic cost is less than or equal to the current lowest heuristic cost, save generated child and update current lowest heuristic cost 
				if (temp != board):
					if (temp_h_cost < currHeuristicCost):
						child = temp.copy()
						currHeuristicCost = temp_h_cost
					elif (temp_h_cost == currHeuristicCost):
						same_cost_children.append(temp)
						x = random.randint(0, len(same_cost_children)-1)
						child = same_cost_children[x]
			else:
				# if sideways moves are not allowed, and the generated child heuristic cost is less than the current lowest heuristic cost, save generated child and update current lowest heuristic cost
				if (temp != board) and (temp_h_cost < currHeuristicCost):
					child = temp.copy()
					currHeuristicCost = temp_h_cost
	return child

#Main function
def main():
	startTime = time.process_time()
	# n is the number of queens in the N Queen Puzzle which is input by the user
	n = input("Enter an integer for the size of the board: ")
	n=(int)(n)
	print('Using Hill Climbing Algorithm for n=',n)
	#sucess rate = success count/number of iterations
	success_rate = False
	#success_count gives the number of times hill climbing gives the optimal result
	success_count = 0
	#failure_count gives the number of times hill climbing does not give the optimal result
	failure_count = 0
	for i in range(3):
		print('Run ' + str(i + 1) + ':')
		step_count, success = HillClimbing(generateRandomBoard(n), n, verbose=True)
		if (success):
			print('Success.')
			success_count += step_count
		else:
			print('Failure.')
			failure_count += step_count
		success_rate += success
	for i in range(3, iterations):
		step_count, success = HillClimbing(generateRandomBoard(n), n)
		if (success):
			success_count += step_count
		else:
			failure_count += step_count
		success_rate += success

	#printing the output of the algorithm
	endTime = time.process_time()
	print('Using Hill Climbing Algorithm for n = ',n)
	print('The following result is obtained')
	print('Success rate: ' + str(success_rate/iterations))
	print('Failure rate: ' + str(1-(success_rate/iterations)))
	print('Average steps until success: ' + str(success_count/success_rate))
	if iterations-success_rate>0 : 
		print('Average steps until failure: ' + str(failure_count/(iterations - success_rate)))
	print('Total Time : '+ str(endTime - startTime))

if __name__ == '__main__':
    main()
k=input("press close to exit")