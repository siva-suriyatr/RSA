'''
@Author - _______________

Write a function in python that takes two integers x and y as arguements and 
returns the greatest common divisor between them. Both iterative and recursive 
methods are allowed. 

Use Euclid's Algorithm to arrive at the answer. 

Explore the concept of tuples in python. In short, python has a data structure 
where multiple assignments can be done at once. For example, 

x, y = y, x + y

is equivalent to  

temp = x
x = y
y = temp

The function should return the resultant GCD integer. NOTE: Only Euclid's algorithm must be used to 
implement the function.

Sample Output: 
gcd(12, 10) returns 2
gcd(12, 13) returns 1
'''

def gcd(a, b):
    
    return gcd