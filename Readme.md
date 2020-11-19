### N QUEENS PROBLEM
*using hill climbing, hill climbing with random restart and simulated annealing*

## Problem Description : 
Given a NXN chessboard, our task is to place n queens on the board in such a way that no two queens attack each other. In chess, queens can attack each other in any direction : horizontally, vertically or diagonally. Two queens can attack each other when they are placed along the same row, same column or same diagonal.

## Hill Climbing : 
The hill climbing algorithm is a greedy algorithm, since the search is carried out in the direction where the value of the cost function is optimized. All the neighbours of the current configuration are analyzed and the algorithm moves in the direction of the neighbour that optimizes the cost function. This successor may not lead to the most optimal solution, but good heuristics will definitely lead to a locally optimal solution. 

## Hill Climbing with Random Restart 
The major shortcoming of the hill climbing algorithm is that it gets stuck on local maxima.The hill climbing algorithm does not allow us to go to a state whose value of the cost function is less optimal than that of the current state, because of which we cannot escape the local maxima once we reach it. 
This problem is resolved through a slight improvement in the hill climbing algorithm - hill climbing with random restart, also known as the shotgun hill climbing. In this algorithm, as and when we reach the local maxima, we start from any random state and proceed till we reach the goal state. 

## Simulated Annealing 
SA can also be considered as hill climbing with random walks made in some specific fashion. Except for going through all the neighbours, we pick one neighbour randomly and take a decision on the basis of whether or not it improves the objective function. If it does improve the objective function, consider this move and repeat the process. Else, consider it as a worse neighbour and take this move with some probability proportional to the objective function.


There are following files in this repository:-
1. HillClimbing.py
This file contains the code of the hill climbing algorithm. The program takes input n from the user and generates the result for n queens problem.

2. HillClimbingRandomRestart.py
This file contains the code of the hill climbing random restart algorithm. The program takes input n from the user and generates the result for n queens problem.

3. SimulatedAnnealing.py
This file contains the code of the simulated annealing algorithm. This program takes nQueensTest.txt file as input and generates the output in result.txt file.

4. There are three test cases file for simulated annealing.  
nQuuensTest.txt : (n=4)
nQuuensTest(1).txt : (n=8)
nQuuensTest(2).txt : (n=9)



