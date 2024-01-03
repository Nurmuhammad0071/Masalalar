#136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
         result ^= num
        return result
#58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       text = s.split()
       t =  text[-1]
       return len(t)
#66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        ls = str(digits[-1])
        digits.pop()
        for lists in ls:
            ints = int(lists)
            digits.append(ints)
        return digits
# 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = haystack.find(needle)
        return a

# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lists = []

        for i in nums:
            if target in nums:
                return nums.index(target)
                break
            elif target is not nums:
                lists.append(i)

        else:
            lists.append(target)
            lists.sort()
            return lists.index(target)


