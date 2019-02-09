import sys
import time

BOARD_SIZE = 20
arg_count=0
def under_attack(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))
#count the LSV for each value
# def least_constraint_value():
#

def rsolve(queens, n):
    global arg_count
    if n == len(queens):
        return queens
    else:
        #define/call csp
        for i in range(n):
            if not under_attack(i,queens):
                arg_count = arg_count + 1   #the number of arguments are being counted.
                newqueens = rsolve(queens+[i],n)
                if newqueens != []:
                    return newqueens
        return []# FAIL

def print_board(queens):
    row = 0
    n = len(queens)
    for pos in queens:
        for i in range(pos):
            sys.stdout.write( ". ")
        sys.stdout.write( "Q ")

        for i in range((n-pos)-1):
            sys.stdout.write( ". ")
        print('')


time_start = time.time()

ans=rsolve([],BOARD_SIZE)
print_board(ans)
print("The total number of arguments : %i" %arg_count)        #printing the total number of arguments
print("Total time taken is : %s" %(time.time()- time_start))  #time taken to run the program.