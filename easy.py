# 1422. Maximum Score After Splitting a String
class Solution(object):
    def maxScore(self, s):
        current = s.count('1')
        max_score = 0
        for char in s[:-1]:
            if char == '1':
                current -= 1
            else:
                current += 1
            if current > max_score:
                max_score = current
        return max_score
