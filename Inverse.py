'''
@Author - _______________

The modular multiplicative inverse is an integer X such that:

A X ≅ 1 (mod M)   

Note: The value of X should be in the range {1, 2, … m-1}, i.e., in the range of integer 
modulo M. ( Note that X cannot be 0 as A*0 mod M will never be 1). The multiplicative inverse 
of “A modulo M” exists if and only if A and M are relatively prime (i.e. if gcd(A, M) = 1)

One way to do this is to try all numbers from 1 to m. For every number x, check if (A * X) % M is 1.
Check for more ways to optimize finding modular multiplicative inverses. Explore the Extended Euclidian
Algorithm to find multiplicative inverses as a start. Bonus points will be provided if you are able to implement
an entended euclidian version of this function. 

Write a function that returns the multiplicative inverse (d) given e and Φ are the arguements. 

e.d ≡ 1 mod Φ(N)

The function should return the integer value d, which is the multiplicative inverse of 'e' in 
the 'phi' space. 

Sample Output: 
multiplicative_inverse(3, 20) returns 7

'''
def multiplicative_inverse(e, phi):
    
    return d

    


