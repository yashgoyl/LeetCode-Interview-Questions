class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        dic = collections.Counter(barcodes)
        index, n = 0, len(barcodes)
        a = [0]*n
        for val, freq in dic.most_common():
            for _ in range(freq):
                if index >= n:
                    index = 1
                a[index] = val
                index+=2
                
        return a
        
