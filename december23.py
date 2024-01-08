#2706. Buy Two Chocolates
class Solution2706(object):
    def buyChoco(self, prices, money):
        min_1 = money
        min_2 = money
        for price in prices:
            if price >= min_2:
                continue
            if price < min_1:
                min_2 = min_1
                min_1 = price
                continue
            min_2 = price
        _sum = min_1 + min_2
        if _sum > money:
            return money
        return money - _sum


#1637. Widest Vertical Area Between Two Points Containing No Points
class Solution1637(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort(key=lambda student: student[0])
        delta = 0
        previous_point = points[0][0]
        i = 1
        len_points = len(points)
        while i < len_points:
            current_point = points[i][0]
            delta = max(delta, current_point - previous_point)
            previous_point = current_point
            i += 1
        return delta


# 1422. Maximum Score After Splitting a String
class Solution1422(object):
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
