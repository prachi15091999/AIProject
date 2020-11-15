
import time
import random
import math

FAILED = False

def getCollisionNum(board):
    #number to count the number of collisions in the given configuration
    number = 0
    for col in range(len(board)):
        for anotherCol in range(col+1, len(board)):
            #if the quuen collide in the same row then increment the number
            if board[col] == board[anotherCol]:
                number += 1 
         #if the quuen collide in the diagonally then increment the number
            elif abs(board[col] - board[anotherCol]) == (anotherCol - col):
                number += 1 
    return number

# accept the random choice with certain probability
def step_SimulatedAnnealing(board):
    #Initialize T as the annealing schdule
    T= len(board)**2
    #annealing scheduling rate 
    rateofannealing = 0.95
    #loop until we find the good state than the current state or there are no opertaor left to be applied in the current state of board
    while True:
        #randomr takes the new random row 
        randomr = random.randint(0,len(board)-1)
        #randomc takes the new random column
        randomc = random.randint(0,len(board)-1)
        #origincollision get the number of collisions in the current state of board
        origincollision = getCollisionNum(board)
       #originrow stores the current state value
        originrow = board[randomc]
        #changing of board congfiguration to new state
        board[randomc] = randomr
        #newcollision get the number of collisions in the new state of board
        newcollision = getCollisionNum(board)
        T = max(T * rateofannealing, 0.02)
        #if new state is better than current state then return this new state of board as in new state there are less collisions
        if newcollision < origincollision:
            return board
        # if new state is not better state than the current state than check the chances of new state to become current state
        else:
            # diff is the difference between new state and current state on the basis of collisions in new state -collisions in current state
            diff = newcollision - origincollision
            # Probality is the Probality of the new state to become the current state
            Probability = min(math.exp(diff / T), 1)
            #if this Probabilityis greater than the random then return this state of board
            if random.random() <= Probability:
                return board
            #if this Probability is less than the random than changes the congfiguration of  the board of the current state which is changed above to the new state
            else:
                board[randomc] = originrow
    
    return board

def solution_SimulatedAnnealing(board):
    # It is the max no of attempts upto which the program calculate the ans and the success rate will increase by increasing the maxRound
    maxRound = 1000000
    count = 0
    while True:
        #Checking for the initial state it is good state or not
        #Cnum gets the whether the given positions of queen on  board result in collision or not if Cnum==0 then there is no collision and the given configuration is safe else there is a collision between queens
        Cnum = getCollisionNum(board)
        if Cnum == 0:
            return board
        #if Cnum is not zero means collision is there so we use step_Annealing function to get better state than  the current state
        board = step_SimulatedAnnealing(board)
        #count is the number which counts the value how many times we change the current state to new state by annealing algorithm
        count += 1
        #if this count is greater than the maxRound then return failed as we are failed to get the solution
        if(count >= maxRound):
            global FAILED
            FAILED = True
            return board
    
def main():
    # n is the board measurement as n*n taken by the user starting from 0
    print("Enter the value of columns starting from 0 of each row in which queen is placed in a nQueensTest file\n")
    
    print("NQueens_hill_climbing_Simulated_Annealing result:\n")
    #starttime is the time when the process starts
   
    startTime = time.process_time()
    
    #sCase = how many times it can find  optimal solution
    sCase = 0
    #tCase=total no of cases to be tested
    tCase = 0
   #result shows all the results of this code
    result=""
    #ans stores all the ans and written in result.textfile
    ans=""
    with open("nQueensTest.txt", "r") as ins:
        for line in ins:
            
            ans=ans+'\n'+"Case :"+str(tCase)+ " is for n = "
            global FAILED
            FAILED = False
            
            # it is the board matrix on which the queens are placed
            board = []
            for col in line.split():
                board.append(int(col))
               
            #pass the given configuration to Annealing function
            board = solution_SimulatedAnnealing(board)
            tCase += 1
            # if the program failed to get teh ans in max 1000000 rounds
            if FAILED:
                ans=ans+str(len(board))+'\n'
                print( "Case: ", tCase-1," is for n =",len(board)," ")
                result += "The program failed to get the ans"
                
            #if the program succesfully finds the ans
            else:
                #Increase the succes case by 1 if the test case succeed to fi d the ans
                sCase += 1
                ans=ans+str(len(board))+'\n'
                print( "Case: ", tCase-1," is for n =",len(board)," ")
                
               
                for col in range(len(board)):
                    result += str(board[col]) + " "
            result += "\n"
            print (result)
            ans=ans+result
            result=""
   # entime is the time at which  results of all test case are coming after getting executed 
    endTime = time.process_time()
    #append the total time to the result
    result += "Total time taken by the program to get the result of all test cases is : " + str(endTime - startTime) + '\n'
     #append the total case and total succes case to the result
    result += "Total cases given by user: " + str(tCase) + '\n' "Total  Success cases in the given set of test cases : " + str(sCase) + '\n'
    # append the succes rate to the result
    result += "Success rate of the program is : " + str(sCase / float(tCase)) + '\n'
    print (result)
    #writing all answers in the ans which is being written in result text file
    ans=ans+result
   #open result text file
    f = open('result.txt', 'w')
    #writing ans in file
    f.write(ans)
    #close file
    f.close()
        
if __name__ == '__main__':
    main()

k=input("press close to exit") 