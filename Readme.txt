#### N QUEENS PROBLEM
*using hill climbing, hill climbing with random restart and simulated annealing*

## Description : 
1. *Given a NXN chessboard, our task is to place n queens on the board in such a way that no two queens attack each other. In chess, queens can attack each other in any direction : horizontally, vertically or diagonally. Two queens can attack each other when they are placed along the same row, same column or same diagonal.*

## Hill Climbing : 
*The hill climbing algorithm is a greedy algorithm, since the search is carried out in the direction where the value of the cost function is optimized. All the neighbours of the current configuration are analyzed and the algorithm moves in the direction of the neighbour that optimizes the cost function. This successor may not lead to the most optimal solution, but good heuristics will definitely lead to a locally optimal solution. *

## Hill Climbing with Random Restart 
*The major shortcoming of the hill climbing algorithm is that it gets stuck on local maxima.The hill climbing algorithm does not allow us to go to a state whose value of the cost function is less optimal than that of the current state, because of which we cannot escape the local maxima once we reach it. 
This problem is resolved through a slight improvement in the hill climbing algorithm - hill climbing with random restart, also known as the shotgun hill climbing. In this algorithm, as and when we reach the local maxima, we start from any random state and proceed till we reach the goal state. *

## Simulated Annealing 










There are following files in this repository:-
1)HillClimbing.py
It is our code of the hill climbing algorithm in pyhton language.To test it for various cases just run it and enter the value of n.Then it shows the result.
2)HillClimbingRandomRestart.py
It is our code of the hill climbing with random restart algorithm in pyhton language.To test it for various cases just run it and enter the value of n.Then it shows the result.
3)SimulatedAnnealing.py
It is our code of the simulated annealing hill climbing algorithm in pyhton language.To test it for various cases the test cases should be written in file nQueensTest.txt file and then it will show the results also stored the result in in result.txt file.
4)There are three test cases file for simulated annealing for one for n=4 named as nQueensTest.txt,second for n=8 named as nQueensTest(2).txt,third for n=9 named as nQueensTest(3).txt.
To run these Test cases  from our code first take the file named as nQueenstest.txt then it will run.
5)There are three result files  which shows the results obtainging from the test cases for simulated annealing ,first one result.txt for n=4,second one result(2).txt for n=8,third one result(3).txt for n=9.


