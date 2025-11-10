#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 22:58:07 2025

@author: manuel
"""
#problem 1
Number = int(input(" Please Enter any Number: "))
ans = 0
for i in range(Number):
    if i %3 ==0 or i%5==0 :
        ans+= i
print (ans)    

#problem 2
fib1 =1
fib2 =2
ans = 2
while fib2<4000000:
    fib3 = fib1+fib2
    fib1=fib2
    fib2=fib3
    if fib2 %2 ==0:
        ans += fib2
print(ans)
    


#problem 3
Number = int(input(" Please Enter any Number: "))
i = 1

while(i <= Number):
    count = 0
    if(Number % i == 0):
        j = 1
        while(j <= i):
            if(i % j == 0):
                count = count + 1
            j = j + 1
            
        if (count == 2):
            print(" %d is a Prime Factor of a Given Number %d" %(i, Number))
    i = i + 1
    
# problem 4
largest = 0
def palindrome(Q:int) -> bool:
    res = str(Q) == str(Q)[::-1]
    return res
for i in range(100,1000):
    for j in range(100,1000):
        z = i*j
        if (palindrome(z) and z> largest):
            largest = z
print(largest)
        
#problem 5
from math import floor

#check if number is prime
def is_prime(n:int) -> bool:
    for x in range(2,floor(n**0.5)+1):
        if n%x ==0:
            return False
    return True
limit =20
primes = [x for x in range(2,limit+1) if is_prime(x)]  
    
def prime_factors(n):
    result = {prime: 0 for prime in primes}
    i = 0
    for prime in primes:
        while n % prime == 0:
            result[prime] += 1
            n = n / prime
    return result

# Initialize factors. We know each prime below limit shows up at least once.
factors = {prime: 1 for prime in primes}

# Look at the prime counts for each number in our range and keep the highest.
for x in range(2, limit + 1):
    for prime, count in prime_factors(x).items():
        factors[prime] = max(count, factors[prime])

# Calculate and print the result.
result = 1
for prime, count in factors.items():
    result *= prime ** count

print(result)


#problem 6

n=100
summer =0
for i in range(0,n+1):
    summer+=i**2

ans = ((n+1)*(n/2))**2 - summer
print(int(ans))

#problem 7

def primes(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]

#problem 8
from functools import reduce
from operator import mul
#largest multiple of 13 adjacent digits
digits= "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

digits = digits.replace('\'', "" )
#use some tricks of the 0s to eliminate the number
adjacentLength = 13
largestProduct = 0

for i in range(0, len(digits) - adjacentLength + 1):

  product = 1

  for j in range(i, i + adjacentLength):
    product *= int(digits[j: j + 1])

  if product > largestProduct:
    largestProduct = product

print (largestProduct)
       

#problem 9
val=1000
for i in range(333):
    for j in range(i+1,500):
        c = val-i-j
        if(i**2+j**2 == c**2):
            print(i,j,c)
#problem 10
def p10(n=2000000):
	r = int(n**0.5)
	assert r*r <= n and (r+1)**2 > n
	V = [n//i for i in range(1,r+1)]
	V += list(range(V[-1]-1,0,-1))
	S = {i:i*(i+1)//2-1 for i in V}
	for p in range(2,r+1):
		if S[p] > S[p-1]:  # p is prime
			sp = S[p-1]  # sum of primes smaller than p
			p2 = p*p
			for v in V:
				if v < p2: break
				S[v] -= p*(S[v//p] - sp)
	return S[n]

#problem 11
"""
x=8 2 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 4 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48]
    """




#problem 16
# 2**1000 = (2**2)**500 = 16**250 = 256**125 =65536**75

s=2**1000
s2=str(s)
summer=0
for i in range(len(s2)):
    summer+=int(s2[i])
print(summer)
    


#problem 20
import math

s=math.factorial(100)
s2=str(s)
counter = 0
for i in range(len(s2)):
    counter += int(s2[i])
    
print(counter) 


#problem 21
d=1000
s=[]
for i in range(1,d+1):
    if d%i==0:
        s.append(i)
print(s)

#problem #25
from math import log10, ceil
def euler25(k):
    if k < 2:
        return 1
    ϕ = (1 + 5**0.5) / 2
    return ceil((k + log10(5) / 2 - 1) / log10(ϕ))
print(euler25(1000))
#problem 29
powerset = set()
for a in range(2,101):
    for b in range(2,101):
        powerset.add(a**b)
print(len(powerset)) 
#9183

       
#problem 34

   