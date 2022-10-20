'''
@Author - _______________

Write a function that takes two integers as arguements and ultimately returns a keypair tuple
as the resultant.

* Take the two arguements and check if both of them are prime by importing and using the 
is_prime function from the isPrime file.

* Make sure that both the arguements are not the same prime number.

    Exit out of the program if either of these conditions are true.

* Calculate N and phi

* Assign a random number to a variable 'e' using the randrange function from the builtin 
random module. Make sure that the value of 'e' is in the range (1, phi). This can be controlled
in the arguements to the randrange function.

* Check if the value 'e' and phi are coprimes using the gcd function from the GCD module.

* If they are not coprimes (i.e., GCD(e, phi) != 0), then keep assigning different values to 
'e' until using the randrange function in a loop until the coprimes condition holds true.

* Calculate a value 'd' for the given values 'e' and phi using the multiplicative_inverse function
from the Inverse Module.

* Return the values generated as a tuple of tuples. 

=>Expected calling function = 

public_key, private_key = generate_key_pair(p, q)

=> Expected return =

return ((e,n) , (d,n))


'''

from isPrime import is_prime
from GCD import gcd
from Inverse import multiplicative_inverse
import random

def generate_key_pair(p, q):

    return ((e, n), (d, n))