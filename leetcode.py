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

# 67. Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
         return bin(int(a, 2) + int(b, 2))[2:]
# 169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            candidate = None
            count = 0

            for num in nums:
                if count == 0:
                    candidate = num
                count += (1 if num == candidate else -1)

            return candidate

# 203. Remove Linked List Elements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to simplify the code
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next
# 206. Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            next_node = current.next
            current.next = prev
            prev, current = current, next_node

        return prev
# 2942. Find Words Containing Character
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for index, word in enumerate(words):
            if x in word:
                result.append(index)
        return result        
# 1662. Check If Two String Arrays are Equivalent
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        lists1 = ""
        lists2 = ""
        for i in word1:
            if i is not lists1:
                lists1 += i

        for i in word2:
            if i is not lists2:
                lists2 += i
        if lists1 == lists2:
            return True
        else:
            return False
# 1816. Truncate Sentence
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ls = s.split()
        string = ""
        for i in range(k):
            i += 1
            string += ls[i - 1]
            if i == k:
                string += ""
            else:
              string += " "
        return string
# 709. To Lower Case
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
#1859. Sorting the Sentence
class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(word[:-1] for word in sorted(s.split(), key=lambda x: int(x[-1])))
# 557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        result = ' '.join(reversed_words)
        return result
