class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # def mergeSort(self, itr):

        #     arr=itr
        #     if len(arr)>1:
        #         mid=len(arr)//2
        #         left=arr[:mid]
        #         right=arr[mid:]

        #         mergeSort(self,left)
        #         mergeSort(self,right)

        #         i=j=k=0

        #         while i<len(left) and j<len(right):
        #             if left[i]<=right[j]:
        #                 arr[k]=left[i]
        #                 i+=1
        #             else:
        #                 arr[k]=right[j]
        #                 j+=1
        #             k+=1

        #         while i<len(left):
        #             arr[k]=left[i]
        #             i+=1
        #             k+=1
        #         while j<len(right):
        #             arr[k]=right[j]
        #             j+=1
        #             k+=1
        #     return "".join(arr)
        # if mergeSort(self,list(s)) == mergeSort(self,list(t)):
        #      return True

        # SECOND ATTEMPT

        # Key concept here is you can check for ANAGRAM either by sorting the string and checking if it is equal or by a hashmap keeping counts or each character for both the strings and then checking if the count matches for each character in both strings.

        if "".join(sorted(s)) == "".join(sorted(t)):
            return True
        return False



