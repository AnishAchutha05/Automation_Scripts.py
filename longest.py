class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for n in num_set:
            # Check if n is the START of a sequence
            if (n - 1) not in num_set:
                length = 1
                # While the NEXT number exists, keep going
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
                
        return longest