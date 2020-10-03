class Solution:
    def countPrimes(self, n: int) -> int:
        primeList = []
        for x in range(2,n):
            isPrime = True
            for y in range(2, int(x ** 0.5) + 1):
                if x % y == 0:
                    isPrime = False
                    break
            if isPrime:
                primeList.append(x)
        return len(primeList)

obj = Solution()
print(obj.countPrimes(10000))