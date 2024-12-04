
# 1. find second smalest and second largest
"""
a = [5,24,54,21,65,45,85,47]
a.sort()
print(a, end="\n")
print(a[1],"  ", a[-2])

"""


# 2. find sum and average exercise time of a person in a week input: 30,40,50,35,45,30,40,

"""
time= [30,40,50,35,45,30,40]

sum=0
week=0

for i in time:
    sum+=i
    week+=1
    
print(time)
print(sum)
print(sum/week)
"""


# 3. Given an integer N, your task is to calculate the sum of the first 10 multiples of N and print the result input 10
"""
n =int(input("entre your number "))
sum =0
for i in range(1, n+1):
    multiple= n*i
    sum+=multiple

print(sum)
"""

# 4. find second largest numbre from the Array
"""
import array

arr1 = array.array('i', [4, 5, 1, 3, 8])

class solution:
    def gfg(self, arr):
        
        a = list(set(arr))
        a.sort()
        return a[-2]


s = solution()
x = s.gfg(arr1)
print(x)

"""

# 5. check s1 all character are same to s2 
"""
from collections import Counter

s1 = 'asif'
s2 = 'fias'

class Solution:
    # Function to check whether two strings are anagrams of each other or not.
    def areAnagrams(self, s1, s2):
        # If lengths of the two strings are not the same, they cannot be anagrams
        if len(s1) != len(s2):
            return False
        
        # Count the frequency of each character in both strings
        #return sorted(s1) == sorted(s2)  # Methord 1  
        return Counter(s1) == Counter(s2) # Methord 2

s = Solution()
x = s.areAnagrams(s1,s2)
print(x)

"""


# 6. Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
# Note: The input strings may contain leading zeros but the output string should not have any leading zeros.
"""
s1 = "1101"
s2 = "111"

class Solution:
    def addBinary(self, s1, s2):
        # Step 1: Convert binary strings to decimal
        num1 = int(s1, 2)
        num2 = int(s2, 2)

        print(num1)
        print(num2)
        
        # Step 2: Add the numbers
        result = num1 + num2
        print(result)
        
        # Step 3: Convert the sum back to binary and strip the '0b' prefix
        binary_result = bin(result)[2:]
        
        # Step 4: Return the result
        return binary_result

s = Solution()
x = s.addBinary(s1,s2)
print(x)
"""



# 7. Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.
# Note: When you return '$' driver code will output -1. 
# Mediam Lavel
#Flipkart, Amazon, Microsoft, D-E-Shaw, MakeMyTrip, Ola Cabs, Payu, Teradata, Goldman Sachs, MAQ Software, InfoEdge, OATS Systems, Tejas Network
"""
s = "geeksforgeeks"

class Solution:
    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):
        # Step 1: Create a frequency dictionary
        freq = {}
        
        # Step 2: Count frequency of each character
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Step 3: Find the first character with frequency 1
        for char in s:
            if freq[char] == 1:
                return char
        
        # Step 4: If no non-repeating character is found, return '$'
        return '$'

# Example usage:
sol = Solution()
print(sol.nonRepeatingChar(s))  # Output should be 'f'
"""

# 8.Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.
# Note: Consider the array as circular.
# Mediam Lavel
# MAQ Software, Amazon, Microsoft

"""
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2

class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  # Ensure that d is less than n
        
        # Helper function to reverse a part of the array
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse the first d elements
        reverse(0, d - 1)
        
        # Step 2: Reverse the remaining elements
        reverse(d, n - 1)
        
        # Step 3: Reverse the entire array
        reverse(0, n - 1)
        
sol = Solution()
sol.rotateArr(arr, d)
print(arr)  # Output should be [3, 4, 5, 6, 7, 1, 2]

"""


# Given two strings, one is a text string txt and the other is a pattern string pat.
# The task is to print the indexes of all the occurrences of the pattern string in the text string.
# Use 0-based indexing while returning the indices. 
# Note: Return an empty list in case of no occurrences of pattern.
# Microsoft
"""
txt = "geeksforgeeks"
pat = "geek"
class Solution:
    def search(self, pat, txt):
        # code here
        result = []
        n = len(txt)
        m = len(pat)
        
        # Iterate through the text and check for the pattern
        for i in range(n - m + 1):
            if txt[i:i + m] == pat:
                result.append(i)
        
        return result


s = Solution()
a = s.search(pat,txt)
print(a)
"""


# Given an array of integers arr[] representing a permutation,
#  implement the next permutation that rearranges the numbers into the lexicographically next greater permutation.
#   If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

# Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

#Infosys, Flipkart, Amazon, Microsoft, FactSet, Hike, MakeMyTrip, Google, Qualcomm, Salesforce

"""
arr = [1, 2, 3, 6, 5, 4]
class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        
        # Step 1: Find the first decreasing element from the end
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find the element just larger than arr[i] from the end
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            
            # Step 3: Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
        
        # Step 4: Reverse the elements after index i
        arr[i + 1:] = arr[i + 1:][::-1]
        
        return arr


s = Solution()
a= s.nextPermutation(arr)
print(a) # output 1 2 4 3 5 6
"""


# You are given an array of integer arr[] where each number represents a vote to a candidate.
# Return the candidates that have votes greater than one-third of the total votes,
# If there's not a majority vote, return an empty array. 

# Note: The answer should be returned in an increasing format.  # Medium


"""

class Solution:
    def findMajority(self, arr):
        # Phase 1: Boyer-Moore Voting Algorithm to find two potential candidates
        if not arr:
            return []
        
        # Initialize two candidates and their counts
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        # First pass to find two potential candidates
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Phase 2: Verify the candidates by counting their occurrences
        count1, count2 = 0, 0
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        # Find the threshold for more than one-third
        threshold = len(arr) // 3
        result = []
        
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)
        
        # Return the sorted result
        return sorted(result)


# Example 1
solution = Solution()
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(solution.findMajority(arr))  # Output: [4]

# Example 2
arr = [1, 1, 1, 3, 3, 2, 2, 2]
print(solution.findMajority(arr))  # Output: [2]

"""



# Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.

# Note: A palindrome string is a sequence of characters that reads the same forward and backward.
#Medium Level

"""

class Solution:
    def minChar(self, s: str) :
        # Function to compute the prefix function (KMP algorithm)
        def compute_prefix_function(s):
            n = len(s)
            pi = [0] * n
            for i in range(1, n):
                j = pi[i - 1]
                while j > 0 and s[i] != s[j]:
                    j = pi[j - 1]
                if s[i] == s[j]:
                    j += 1
                pi[i] = j
            return pi
        
        # Reverse the string
        rev_s = s[::-1]
        
        # Concatenate original string and reverse string with a separator in between
        combined = s + '#' + rev_s
        
        # Compute the prefix function for the combined string
        pi = compute_prefix_function(combined)
        
        # The number of characters to add is the difference between the length of s
        # and the length of the longest matching prefix-suffix.
        longest_prefix_suffix = pi[-1]
        
        # Return the number of characters to be added at the front
        return len(s) - longest_prefix_suffix


# Example 1
solution = Solution()
s = "aacecaaa"
print(solution.minChar(s))  # Output: 2 (We need to add "aa" in front)

# Example 2
s = "abcd"
print(solution.minChar(s))  # Output: 3 (We need to add "dcb" in front)
"""

# The cost of stock on each day is given in an array price[].
# Each day you may decide to either buy or sell the stock at price[i], 
# you can even buy and sell the stock on the same day. Find the maximum profit that you can get.
# Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.
# Hard Lavel
# Paytm, Flipkart, Morgan Stanley, Accolite, Amazon, Microsoft, Samsung, D-E-Shaw, Hike, Make MyTrip, Ola Cabs, Oracle, Walmart,
# Goldman Sachs, Directi, Intuit, SAP Labs, Quikr, Facebook, Salesforce, Pubmatic, Sapient, Swiggy

"""
prices= [100, 180, 260, 310, 40, 535, 695]

class Solution:
    def maximumProfit(self, prices) -> int:
        # Initialize variable to keep track of the total profit
        profit = 0
        
        # Iterate through the prices array and add up all the profitable price increases
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit

s = Solution()
x = s.maximumProfit(prices)
print(x)

"""

# You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.
# Note: The characters in the strings are in lowercase.
# Easy Lavel # Oracle, Adobe

"""
s1 = "abcd"
s2 = "cdab"

class Solution:
    # Function to check if two strings are rotations of each other or not.
    def areRotations(self, s1, s2):
        # If the lengths of the strings are not equal, they cannot be rotations
        if len(s1) != len(s2):
            return False
        
        # Concatenate s1 with itself and check if s2 is a substring of this concatenated string
        if s2 in (s1 + s1):
            return True
        return False

s = Solution()
x = s.areRotations(s1,s2)
print(x)

"""



