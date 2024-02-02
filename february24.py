#1291. Sequential Digits
class Solution1291(object):
    def sequentialDigits(self, low, high):
        start_digit, start_len = self.get_start_sequential(low)
        start_len += len(str(low))
        end_start_digit, end_len = self.get_end_sequential(high)
        end_len += len(str(high))
        if start_len > end_len or (start_len == end_len and end_start_digit < start_digit):
            return []
        if start_len == end_len:
            return self.get_row(start_len, start_digit, end_start_digit)

        end = 10 - start_len
        sequential_digits = self.get_row(start_len, start_digit, end)

        while start_len + 1 < end_len:
            start_len += 1
            end -= 1
            sequential_digits += self.get_row(start_len, 1, end)
        
        sequential_digits += self.get_row(start_len + 1, 1, end_start_digit)
        return sequential_digits

    def get_row(self, digits, start_digit, end_digit):
        row_len = end_digit - start_digit + 1
        row = [0]*row_len
        delta = int('1'*digits)
        i = start_digit
        current = 0
        while i < digits + start_digit:
            current = current*10 + i
            i += 1
        i = 0
        while i < row_len:
            row[i] = current
            current += delta
            i += 1
        return row


    def get_start_sequential(self, start):
        start = str(start)  
        current = ord(start[0])
        start_digit = current - ord('1') + 1
        if start_digit - 1 + len(start) > 9:
            return 1, 1
        for char in start:
            if ord(char) == current:
                current += 1
                continue
            if ord(char) > current:
                if start_digit - 1 + len(start) > 9:
                    return 1, 1
                return start_digit + 1, 0
            break
        return start_digit, 0


    def get_end_sequential(self, start):
        start = str(start)  
        current = ord(start[0])
        start_digit = current - ord('1') + 1
        if start_digit - 1 + len(start) > 9:
            return 10 - len(start), 0
        for char in start:
            if ord(char) == current:
                current += 1
                continue
            if ord(char) < current:
                if start_digit == 1:
                    return 10 - len(start) + 1, -1
                if start_digit - 1 + len(start) > 9:
                    return 10 - len(start), 0
                return start_digit - 1, 0
            break
        return start_digit, 0


#2966. Divide Array Into Arrays With Max Difference
class Solution2966:
    def divideArray(self, nums, k):
        SIZE = 3
        nums.sort()
        len_arr = len(nums)
        result_array = [0]*(len_arr // SIZE)
        i = 0
        while i < len_arr:
            if nums[i+2] - nums[i] > k:
                return []
            result_array[i // 3] = nums[i:i+3]
            i += 3
        return result_array
  