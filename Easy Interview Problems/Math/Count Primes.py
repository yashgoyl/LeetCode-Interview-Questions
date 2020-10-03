class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        primeCount = 0
        for i in range(2,n):
            if isPrime[i] == True:
                primeCount += 1
                for j in range(i*i, n, i):
                    isPrime[j] = False
        return primeCount 
        
        
obj = Solution()
print(obj.countPrimes(10))  #Ans - 4
