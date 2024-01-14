#872. Leaf-Similar Trees
class Solution872(object):
    def leafSimilar(self, root1, root2):
        left = []
        right = []
        self.getLeaves(root1, left)
        self.getLeaves(root2, right)
        return left == right

    def getLeaves(self, root, leaf_arr):
        if not root:
            return
        if not root.left and not root.right:
            leaf_arr.append(root.val)
            return
        self.getLeaves(root.left, leaf_arr)
        self.getLeaves(root.right, leaf_arr)


# 2385. Amount of Time for Binary Tree to Be Infected
class Solution2385(object):
    def amountOfTime(self, root, start):
        counting = [0, [0,0]]
        # after start; after root

        # поиск первого разветвления или старта
        count = 0 # перед первым стартом или развилкой
        current = root
        while current.val != start and not(current.left and current.right):
            count += 1
            if current.left:
                current = current.left
                continue
            current = current.right
        # если первый старт
        if current.val == start:
            counting[0] = self.afterStartCounter(current)
        # если первая развилка
        else:
            counting[1] = self.depthCounter(current, start, counting)
        from_start_to_top = count + counting[1][0]
        return max(counting[0], from_start_to_top, counting[1][1])

         
    def depthCounter(self, root, start, counting):
        if not root:
            return [0, 0]
        if root.val == start:
            counting[0] = self.afterStartCounter(root)
            # до start, максимум при этом центровом узле наверх
            return [-1, 0]
        if not root.right and not root.left:
            return [0, 0]
        left = self.depthCounter(root.left, start, counting)
        right = self.depthCounter(root.right, start, counting)
        new_start = 0
        new_max = 0
        if left[0]:
            if left[0] > 0:
                new_start = left[0]
            new_start += 1
            new_max = max(left[1], new_start + right[1]+1)
        elif right[0]:
            if right[0] > 0:
                new_start = right[0]
            new_start += 1
            new_max = max(right[1], new_start + left[1]+1)
        else:
            new_max = max(right[1], left[1])+1
        return [new_start, new_max]
        

    # сюда передавать сам старт
    def afterStartCounter(self, root):
        if not root:
            return 0
        if not root.right and not root.left:
            return 0
        max_left = self.afterStartCounter(root.left)
        max_right = self.afterStartCounter(root.right)
        return max(max_left, max_right) + 1


# 1026. Maximum Difference Between Node and Ancestor
class Solution1026(object):
    def maxAncestorDiff(self, root):
        diff, max_, min_ = self.findMaxDiff(root)
        return diff
    
    def findMaxDiff(self, root):
        if not root:
            return 0, 0, None
        current_ancestor = root.val
        current_min = current_ancestor
        left_diff, left_max, left_min = self.findMaxDiff(root.left)
        right_diff, right_max, right_min = self.findMaxDiff(root.right)
        current_max = max(current_ancestor, left_max, right_max)
        if left_min is not None and left_min < current_min:
            current_min = left_min
        if right_min is not None and right_min < current_min:
            current_min = right_min
        max_diff = max(left_diff, right_diff, current_ancestor - current_min, current_max - current_ancestor)
        return max_diff, current_max, current_min 


# 455. Assign Cookies
class Solution455(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        s_i = 0
        g_i = 0
        s_len = len(s)
        g_len  = len(g)
        while s_i < s_len and g_i < g_len:
            if s[s_i] >= g[g_i]:
                g_i += 1
            s_i += 1
        return g_i


#1657. Determine if Two Strings Are Close
class Solution1657(object):
    def closeStrings(self, word1, word2):
        freq1 = [0]*26
        freq2 = [0]*26
        for char in word1:
            freq1[ord(char)-ord('a')] += 1
        for char in word2:
            freq2[ord(char)-ord('a')] += 1
        i = 0
        while i < 26:
            if (freq1[i] == 0) != (freq2[i] == 0):
                return False
            i += 1
        freq1.sort()
        freq2.sort()
        i = -1
        while i > -27:
            if freq1[i] != freq2[i]:
                return False
            if not freq1[i]:
                break
            i -= 1
        return True
        