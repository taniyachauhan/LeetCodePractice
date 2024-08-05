class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        #         else:
        #             return False
        dict={}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=1
            elif nums[i] in dict:
                dict[nums[i]]+=1

        temp=list(dict.values())
        for j in temp:
            if j>1:
                return True



                
