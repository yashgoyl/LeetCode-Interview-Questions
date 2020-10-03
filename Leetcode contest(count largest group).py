#class Solution:
    #def countLargestGroup(self, n: int) -> int:
        #if n<10:
            #return n
        #a = n//10
        #count = 0
        #for i in range(n,9,-1):
            #copy = n
            #b = n//10
            #tot=0
            #while(copy>0):
                #dig=copy%10
                #tot=tot+dig
                #copy=copy//10
            #if a == b and tot < 10:
                #count += 1
                #n = n-1
            #else:
                #n=n-1
        #return count
#obj = Solution()
#print(obj.countLargestGroup(129))
class Solution:
    def getDigSum(self, n):
            dig = 0
            while n != 0:
                dig += n % 10
                n /= 10
            return dig
        def countLargestGroup(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n < 10:
                return n
            d = {}
            for i in range(1, 10):
                d[i] = 1
            max_val = 0
            for i in range(10, n + 1):
                curSum = self.getDigSum(i)
                if curSum in d:
                    d[curSum] += 1
                    if d[curSum] > max_val:
                        max_val = d[curSum]
                else:
                    d[curSum] = 1
            count = 0
            for key in d:
                if d[key] == max_val:
                    count += 1
            return count


obj = Solution()
print(obj.countLargestGroup(46))