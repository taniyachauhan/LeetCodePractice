# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        def binarySearch(self, k):
            f=0
            l=i
            while f<=l:
                mid=f+(l-f)//2
                if reader.get(mid)==target:
                    return mid
                elif reader.get(mid)< target:
                    f=mid+1
                elif reader.get(mid) > target:
                    l=mid-1
            return -1
        i=0
        while reader.get(i) < target:
            i = 2+i

        return binarySearch(self, i)
        

            