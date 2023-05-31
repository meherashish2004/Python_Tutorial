class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mapset = {}
        for i in nums:
            if i in mapset:
                mapset[i] +=1
            else:
                mapset[i] = 0
        list1 = mapset.keys()
        list2 = list(sorted(mapset.items(), key=lambda kv:
                 (kv[1], kv[0])))
        ans =[]
        i = len(list2)-1
        while k > 0 and i>=0:
            ans.append(list2[i][0])
            i-=1
            k-=1
        

        return ans
