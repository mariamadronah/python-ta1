import sys
import os


#def prime(s):
    # your code goes here

#def solution(s):
    #return prime(s)
#

#if __name__ == "__main__":
   # if len(sys.argv) <= 1:
       # sys.exit(os.error("Argument required"))

    #print(solution(sys.argv[1]))


# Python function that takes a number as a parameter and check the number is prime or not.

def solution(n):  
    # Checking that given number is more than 1  
    if n > 1:  
        # Iterating over the given number with for loop  
        for i in range(2, n):    
            if (n % i) == 0: 
                #print("not primenumber") 
                #break
                return False  
                # False means not a prime number
        else: 
            #print(" primenumber")  
            return True  
            #True means a prime number
    else: 
        #print("not primenumber")  
        return False 

# Taking an input number from the user  
#n = int(input("Enter an input number:"))  
#solution(n)
