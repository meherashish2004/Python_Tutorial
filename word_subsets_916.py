
class Solution(object):
    def wordSubsets(words1, words2):
        ans = set(words1)
        letters_count = {}
        for i in words2:
            for j in i:
                count = i.count(j)
                if j not in letters_count or count > letters_count[j]:
                    letters_count[j] = count
        for i in words1:
            for j in letters_count:
                # print(i,j)
                if i.count(j) < letters_count[j]:
                    ans.remove(i)
                    break
        return list(ans)
    
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]
    list2 = wordSubsets(words1,words2)
    print(list2)
    
    