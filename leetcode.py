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
