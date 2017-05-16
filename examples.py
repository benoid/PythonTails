#!/usr/bin/python

from pygtails import *

# Example 1
# Recursively print a string, popping its
# first element until its length is zero

def recursive_print(str):
    # Create a temporary function 
    # which returns a recursive TailCall 
    # closure object
    def rp(str):
        if len(str) == 0:
           return
        print(str)
        return TailCall(lambda: rp(str[1:]))
    # Create and call a tail call optimized version
    # of the temporary function
    TailCallable(rp)(str)

recursive_print("hello")


# Example 2
#
# Recursive implementation of Sieve of Etatosthenes

def sieve_of_eratosthnes(max):
    def helper(nums, known_primes):
        if len(nums) > 0:
            current_prime = nums[0]
            known_primes.append(current_prime)
            return TailCall(lambda: helper(filter(lambda x: x % current_prime != 0, nums), known_primes))
        else:
            return known_primes
    return TailCallable(helper)(range(2,max + 1), [])

print(sieve_of_eratosthnes(100))
    
