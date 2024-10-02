class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     return self.binarySearch(nums, target)
    # def binarySearch(self, arr, target):
    #     if len(arr)==0:
    #         return [-1,-1]
    #     if len(arr)==1 and target ==arr[0]:
    #         return [0,0]
    #     f = 0
    #     l = len(arr)-1

    #     while f<=l:
    #         mid = (f+l)//2
    #         if arr[mid] == target:
    #             i=k=mid
                
    #             while i<l and arr[i+1]==target:
    #                 i+=1

    #             while k>f and arr[k-1]==target:
    #                 k-=1

    #             if i!=mid and k==mid:
    #                 return [k,i]
    #             elif i!= mid and k!=mid:
    #                 return [k,i]
    #             elif i== mid and k!=mid:
    #                 return [k,i]
    #             elif i==mid and k==mid:
    #                 return [mid, mid]

    #         elif target < arr[mid]:
    #             l = mid-1
    #         elif target > arr[mid]:
    #             f =  mid+1
    #     return [-1,-1]
        def binarySearch(arr, target, findStart):
            l = 0
            r = len(arr) - 1
            idx = -1  # Initialize with -1 to indicate not found
            
            while l <= r:
                mid = l + (r - l) // 2
                
                if arr[mid] == target:
                    idx = mid  # Store the current index
                    if findStart:
                        # If looking for the start index, move left
                        r = mid - 1
                    else:
                        # If looking for the end index, move right
                        l = mid + 1
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return idx
        
        # Call binary search for the start and end indices
        start = binarySearch(nums, target, findStart=True)
        end = binarySearch(nums, target, findStart=False)
        
        return [start, end]


         

