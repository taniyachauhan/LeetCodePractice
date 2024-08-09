class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        '''m_dict={}
        for i in range(len(names)):
            m_dict[heights[i]]=names[i]
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if heights[i]<heights[j]:
                    heights[i],heights[j]=heights[j],heights[i]
        names.clear()
        for i in heights:
            names.append(m_dict[i])
        return names'''

        ## Other way of solving the problem:
        res_dict = {}

        for i in range(len(heights)):
            res_dict[heights[i]] = names[i]
        sorted_keys = sorted(res_dict.keys(), reverse = True)
        print(sorted_keys)
        # return [res_dict[key] for key in sorted_keys]





        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if heights[i]<heights[j]:
                    heights[i],heights[j]=heights[j],heights[i]
                    names[i],names[j]=names[j],names[i]
        return names