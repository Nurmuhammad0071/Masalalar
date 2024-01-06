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
# 1684. Count the Number of Consistent Strings
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0
        for word in words:
            if all(char in allowed_set for char in word):
                count += 1

        return count
# 2000. Reverse Prefix of Word
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = ""
        if word.find(ch) >= 0:
            fnd = word.find(ch)
            revs = word[:fnd + 1]
            strs = revs[::-1]
            result += strs
            ids = word[:fnd:-1]
            result += ids[::-1]
        else:
            return word
        return result
# 2418. Sort the People
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_names = [name for _, name in sorted(zip(heights, names), reverse=True)]
        return sorted_names
# 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''.join([a + b for a, b in zip_longest(word1, word2, fillvalue='')])
        return merged
# 1436. Destination City
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting_cities = set(path[0] for path in paths)
        for _, destination in paths:
            if destination not in starting_cities:
                return destination    
# 1812. Determine Color of a Chessboard Square
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter, number = coordinates[0], int(coordinates[1])
        return (ord(letter) - ord('a') + number) % 2 == 0
# 344. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()
# 1704. Determine if String Halves Are Alike
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        def countVowels(substring):
            return sum(char in vowels for char in substring)

        mid = len(s) // 2
        return countVowels(s[:mid]) == countVowels(s[mid:])
# 2678. Number of Senior Citizens
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                count += 1

        return count
# 657. Robot Return to Origin
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1

        return x == 0 and y == 0
# 2586. Count the Number of Vowel Strings in Range
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set("aeiouAEIOU")
        count = 0
        for i in range(left, right + 1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                count += 1

        return count
# 2278. Percentage of Letter in String
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        total_characters = len(s)
        letter_count = s.count(letter)
        if total_characters == 0:
            return 0
        percentage = (letter_count / total_characters) * 100
        return int(percentage)
# 412. Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        
        return result
# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count
# 1235. Maximum Profit in Job Scheduling
from typing import List
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * len(jobs)
        dp[0] = jobs[0][2]

        for i in range(1, len(jobs)):
            included_profit = jobs[i][2]
            latest_non_overlap = self.find_latest_non_overlap(jobs, i)

            if latest_non_overlap != -1:
                included_profit += dp[latest_non_overlap]

            dp[i] = max(included_profit, dp[i - 1])

        return dp[-1]

    def find_latest_non_overlap(self, jobs, index):
        low, high = 0, index - 1

        while low <= high:
            mid = (low + high) // 2
            if jobs[mid][1] <= jobs[index][0]:
                if jobs[mid + 1][1] <= jobs[index][0]:
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1

        return -1


# 1929. Concatenation of Array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1 = []
        for i in nums:
            nums1.append(i)
        nums.extend(nums1)
        return nums
#dicvhsodivfhordihfvordifhvoifdhvoiurfvhodibvhgrtdoiuhvboldriuhgv