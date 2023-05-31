class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ""
        sorted_list = list(sorted(strs, key = len))
        flag = 0
        count = 0
        for i in range(len(sorted_list[0])):
            for x in sorted_list:
                if sorted_list[0][i] == x[i]:
                    flag = 0
                else:
                    flag = 1
                    break
            if flag == 0:
                prefix = prefix + x[i]
            else:
                break
        return prefix
