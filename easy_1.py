class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for num in nums:
        #     index
        #     find = target - num
        #     for x in nums:
        ans = []
        flag =0
        for index in range(len(nums)):
            find = target - nums[index]
            for i in range(index+1,len(nums)):
                if nums[i] == find:
                    flag =1
                    ans.append(index)
                    ans.append(i)
                    break
            if flag == 1:
                    return ans