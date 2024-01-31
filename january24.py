import random


#380. Insert Delete GetRandom O(1)
class RandomizedSet380(object):

    def __init__(self):
        self.obj_set = []
        self.index_list = {}
    
    def search(self, val):
        return val in self.obj_set

    def insert(self, val):
        if self.search(val):
            return False
        self.obj_set.append(val)
        self.index_list[val] = len(self.obj_set) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False
        del_index = self.index_list[val]
        last_val = self.obj_set[-1]
        self.obj_set[del_index] = last_val
        self.index_list[last_val] = del_index
        self.obj_set.pop()
        del self.index_list[val]
        return True

    def getRandom(self):
        return random.choice(self.obj_set)


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


#1704. Determine if String Halves Are Alike
class Solution1704(object):
    def halvesAreAlike(self, s):
        s = s.lower()
        s_len = len(s)
        half = s_len / 2
        i = 0
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        first_half = 0
        while i < half:
            if s[i] in VOWELS:
                first_half += 1
            i += 1
        while i < s_len:
            if s[i] in VOWELS:
                first_half -= 1
                if first_half < 0:
                    return False
            i += 1
        return not first_half


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


# 2225. Find Players With Zero or One Losses
class Solution2225(object):
    def findWinners(self, matches):
        lose = {}
        for match in matches:
            loser = match[1]
            if match[0] not in lose:
                lose[match[0]] = 0
            if loser not in lose:
                lose[loser] = 1
            elif lose[loser] < 2: 
                lose[loser] += 1
        no_lose = []
        one_lose = []
        for part, loses in lose.items():
            if not loses:
                no_lose.append(part)
                continue
            if loses == 1:
                one_lose.append(part)
        no_lose.sort()
        one_lose.sort()
        return [no_lose, one_lose]

# 1347. Minimum Number of Steps to Make Two Strings Anagram
class Solution1347(object):
    def minSteps(self, s, t):
        s_count = [0]*26
        t_count = [0]*26
        for char in s:
            s_count[ord(char)-ord('a')] += 1
        for char in t:
            t_count[ord(char)-ord('a')] += 1
        steps = 0
        i = 0
        while i < 26:
            if s_count[i] > t_count[i]:
                steps += s_count[i] - t_count[i]
            i += 1
        return steps


#1207. Unique Number of Occurrences
class Solution1207(object):
    def uniqueOccurrences(self, arr):
        arr.sort()
        occurrences = []
        current = arr[0]
        count = 1
        i = 1
        arr_len = len(arr)
        while i < arr_len:
            if arr[i] == current:
                count += 1
                i += 1
                continue
            if count in occurrences:
                return False
            occurrences.append(count)
            count = 1
            current = arr[i]
            i += 1
        return count not in occurrences


#70. Climbing Stairs
class Solution70(object):
    def climbStairs(self, n):
        current_1 = n % 2
        current_2 = n // 2
        ways_counter = 0
        while current_1 < n:
            ways_counter += self.get_combinations(current_1, current_2)
            current_1 += 2
            current_2 -= 1
        return ways_counter + 1 #добавляет 1 для случая только из 1

    def get_factorial(self, n, end = 1):
        if n <= end + 1:  # обрабатывает вариант с 0 и 1
            return n
        return n*self.get_factorial(n-1, end)
    
    def get_combinations(self, n, k):
        return self.get_factorial(n+k, n) / self.get_factorial(k)


#2610. Convert an Array Into a 2D Array With Conditions
class Solution2610(object):
    def findMatrix(self, nums):
        result_array = []
        current_rows = 0
        for char in nums:
            i = 0
            while i < current_rows:
                if char not in result_array[i]:
                    result_array[i].append(char)
                    break
                i += 1
            if i == current_rows:
                result_array.append([char])
                current_rows += 1
        return result_array

#645. Set Mismatch
class Solution645(object):
    def findErrorNums(self, nums):
        nums.sort()
        i = 1
        doubled = 0
        missed = 0
        for num in nums:
            if i == num:
                i += 1
                continue
            if i > num:
                doubled = num
                if missed:
                    return [doubled, missed]
                continue
            missed = i
            i = num + 1
            if doubled:
                return [doubled, missed]
        return [doubled, i]
    
#1457. Pseudo-Palindromic Paths in a Binary Tree
class Solution1457(object):
    def pseudoPalindromicPaths (self, root):
        basic_arr = [0]*9
        if not root:
            return 0
        return self.findPath(root, basic_arr)
    
    def findPath(self, root, basic_arr):
        if not root:
            return 0
        basic_arr[root.val-1] += 1
        if not root.left and not root.right:
            count = int(self.ispseudoPalindromic(basic_arr))
        else:
            count = self.findPath(root.left, basic_arr) + self.findPath(root.right, basic_arr)
        basic_arr[root.val-1] -= 1
        return count

    def ispseudoPalindromic(self, counter):
        unique = 1
        for char in counter:
            if not char % 2:
                continue
            if not unique:
                return False
            unique -= 1
        return True

#1239. Maximum Length of a Concatenated String with Unique Characters
class Solution1239(object):
    def maxLength(self, arr):
        len_arr = len(arr)
        next_str = [0]*len_arr
        i = len_arr - 1
        self.find_not_unique(arr, next_str)
        while i >= 0:
            if next_str[i]:
                i -= 1
                continue
            next_str[i] = []
            j = i - 1
            j=0
            while j < i:
                if next_str[j]:
                    j += 1
                    continue
                common = 1
                for char in arr[j]:
                    if char in arr[i]:
                        common = 0
                        break
                if common:
                    next_str[i].append(j)
                j += 1
            i -= 1
        max_length = 0
        i = len_arr-1
        while i >= 0:
            if next_str[i] == 1:
                i -= 1
                continue
            current_len = len(arr[i])
            variants = next_str[i]
            if not variants:
                if current_len > max_length:
                    max_length = current_len
                i -= 1
                continue
            # для непустого списка вариантов продолжений
            max_tail = 0
            continue_len = len(variants)
            j = continue_len - 1
            while j >= 0:
                current = variants[j]
                current_common = []
                self.find_common(variants, next_str[current], current_common)
                tail_length = len(arr[current])
                tail_length += self.find_chains(arr, next_str, current_common)
                if tail_length > max_tail:
                    max_tail = tail_length
                j -= 1
            max_length = max(max_length, max_tail + current_len)
            i -= 1
        return max_length
    
    def find_chains(self, arr, next_str, current_common):
        if not current_common:
            return 0
        current = current_common.pop()
        if not current_common:
            return len(arr[current])
        # это если оставляем ячейку
        curr_common_1 = []
        self.find_common(current_common, next_str[current], curr_common_1)
        # если убрали ячейку
        len_var_2 = self.find_chains(arr, next_str, current_common)
        len_var_1 = self.find_chains(arr, next_str, curr_common_1)
        #считалка длины по номерам суммируемых элементов
        return max(len(arr[current]) + len_var_1, len_var_2)

    def find_common(self, arr1, arr2, common_arr):
        i = 0
        j = 0
        len_1 = len(arr1)
        len_2 = len(arr2)
        while i < len_1 and j < len_2:
            if arr1[i] == arr2[j]:
                common_arr.append(arr1[i])
                i += 1
                j += 1
                continue
            if arr1[i] > arr2[j]:
                j += 1
                continue
            i += 1

    def only_unique_letters(self, str_):
        unique = []
        for char in str_:
            if char in unique:
                return False
            unique.append(char)
        return True

    def find_not_unique(self, arr, next_str):
        i = 0
        len_arr = len(arr)
        while i < len_arr:
            if not arr[i] or not self.only_unique_letters(arr[i]):
                next_str[i] = 1
            i += 1


#232. Implement Queue using Stacks
MAX_SIZE = 100
class MyQueue(object):
    def __init__(self):
        self.head = 0 # где первый элемент в очереди
        self.tail = 0 # куда вставлять следующий
        self.size = 0
        self.array = [None]*MAX_SIZE

    def push(self, x):
        self.array[self.tail] = x
        self.tail = (self.tail + 1) % MAX_SIZE
        self.size += 1    

    def pop(self):
        current = self.peek()
        self.array[self.head] = None
        self.head = (self.head + 1) % MAX_SIZE
        self.size -= 1
        return current

    def peek(self):
        return self.array[self.head]

    def empty(self):
        return self.size == 0
