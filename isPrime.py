'''
@Author - _______________

Write a function in python that takes an integer x and checks if it is a prime number or not.
This can be done by checking if each number between 1 and x divides x completely and gives a 
remainder of zero.   

Several improvements can be made to this method. 

The range that is checked can be shortened from [ 2 to x-1 ] to [ 2 to squareroot(x) ]
Even further changes like eliminating numbers that are divisible by 2 and 3 and then iterating 
in increments of 6 with a start value of 5 is also possible. 

Explore efficient ways to check is a number is prime or not. 

Time complexitiy/efficiency is not graded.

The function should return True if the number is prime and False otherwise. 

Sample output: 

is_prime(7) returns True
is_prime(20) returns False
'''

def is_prime(num):
    
    #return True

    #return False