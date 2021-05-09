import math
import numpy as np

def is_palyndrome(num):
    num_str = str(num)
    if len(num_str)%2 == 0:
        left_side = num_str[:len(num_str)//2]
        right_side = num_str[len(num_str)//2:]
        if left_side == right_side[::-1]:
            return True;
        else:
            return False
    else:
        left_side = num_str[:len(num_str)//2]
        right_side = num_str[len(num_str)//2+1:]
        if left_side == right_side[::-1]:
            return True;
        else:
            return False
        
def to_binary(n):
    return bin(n)[2:]

def is_prime(n):
    for i in range(2, int(np.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def divisors(n):
    divs = []
    for i in range(1, n//2+1):
        if n % i == 0:
            divs.append(i) 
    return divs

def factorial(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod