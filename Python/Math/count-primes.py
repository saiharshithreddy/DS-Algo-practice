class Solution:
    def countPrimes(self, n: int):
        if n <2:
            return 0
        '''
        sieve of erathoneses algo
        If a num is prime then its multiples are not prime.
        
        Example: N = 10
        nums = [1,2,3,4,5,6,7,8,9,10]
        primes = [2,3,5,7]
        prime multiples = [4,6,8,9,10]
        '''
        
        prime = [True] * (n-1)
        prime[0] = False
        p = 2 # first prime 
        count = 0
        while p*p < n:
            
            if prime[p-1] == True:
                
                for i in range(p*p,n,p):
                    
                    prime[i-1] = False 
                    
            p += 1
        
        for i in range(len(prime)):
            if prime[i] == True:
                count += 1
        return count 
        