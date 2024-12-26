
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


# 9. Given two strings, one is a text string txt and the other is a pattern string pat.
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


# 10 Given an array of integers arr[] representing a permutation,
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


# 11 You are given an array of integer arr[] where each number represents a vote to a candidate.
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



# 12 Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.

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

# 13 The cost of stock on each day is given in an array price[].
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

# 14 You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.
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


# 15. Given an array prices[] of length n, representing the prices of the stocks on different days.
# The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed.
# Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.
# Note: Stock must be bought before being sold.
# Easy Lavel    
# Bloomberg, Facebook, Intel, Infosys, Zoho, Morgan Stanley, Amazon, Microsoft, Samsung, Yahoo, PayPal, Nvidia,
# Oracle, Visa, Walmart, Goldman Sachs, TCS, Adobe, Google, IBM, Accenture, Apple, Uber

"""
class Solution:
    def maximumProfit(self, prices):
        # Edge case: if the prices array is empty or has one price, no profit can be made
        if not prices or len(prices) < 2:
            return 0
        
        # Initialize min_price with a large number and max_profit to 0
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through the prices array
        for price in prices:
            # Update the min_price if we find a new lower price
            if price < min_price:
                min_price = price
            # Calculate the profit if we sell at the current price
            profit = price - min_price
            # Update max_profit if the calculated profit is greater
            if profit > max_profit:
                max_profit = profit
        
        # Return the maximum profit found
        return max_profit


# Example usage:
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maximumProfit(prices))  # Output: 5

"""


# 16. Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Easy Lavel
# Paytm, Flipkart, Morgan Stanley, Amazon, Microsoft, OYO Rooms, Samsung, Snapdeal, Hike,
# MakeMyTrip, Ola Cabs, Walmart, MAQ Software, Adobe, Yatra.com, SAP Labs, Qualcomm

"""
arr= [0, 1, 2, 0, 1, 2]
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        arr.sort()
        
        return arr

s = Solution()
x = s.sort012(arr)
print(x)

"""


# 15. Given an array arr[] denoting heights of N towers and a positive integer K.

# For each tower, you must perform exactly one of the following operations exactly once.

# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by K for each tower. After the operation,
#  the resultant array should not contain any negative integers.
# Mediam Level
# Microsoft, Addobe

"""
arr = [1, 5, 8, 10]
k = 2

class Solution:
    def getMinDiff(self, arr, k):
        # First, sort the array
        arr.sort()

        # Number of towers
        n = len(arr)
	
        res = arr[n - 1]- arr[0]
    
    
        for i in range(1, len(arr)):
            if arr[i] - k <0:
                continue
        
            minH = min(arr[0] + k, arr[i]-k)
    
            maxH = max(arr[i - 1] + k, arr[n-1] -k)
    
            res = min(res, maxH - minH)
    
        return res
s = Solution()
x = s.getMinDiff(arr, k)
print(x)
"""


# 16. Given an integer array citations[], where citations[i] is the number of citations a researcher received for the ith paper.
#  The task is to find the H-index.
# H-Index is the largest value such that the researcher has at least H papers that have been cited at least H times.
# Mediam Level

"""

citations = [6, 5, 3, 1, 0]

class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        # Sort the citations array in non-decreasing order
        citations.sort()
        
        # Initialize hIndex
        n = len(citations)
        hIndex = 0
        
        # Loop through the sorted citations
        for i in range(n):
            # The number of papers with at least 'citations[i]' citations
            # is the number of papers from index 'i' to the end
            if citations[i] >= n - i:
                hIndex = n - i
                break
        
        return hIndex

s = Solution()
x = s.hIndex(citations)
print(x)
"""


# 17. Given an integer array arr[]. You need to find the maximum sum of a subarray.

"""
arr = [2, 3, -8, 7, -1, 2, 3]
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        
        # Initialize variables
        current_sum = arr[0]  # Start with the first element
        max_sum = arr[0]  # Start with the first element
        
        # Loop through the array starting from the second element
        for i in range(1, len(arr)):
            # Update current_sum to be either the current element itself
            # or the current element + previous subarray sum
            current_sum = max(arr[i], current_sum + arr[i])
            
            # Update max_sum if current_sum is greater than max_sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum

s = Solution()

x = s.maxSubArraySum(arr)
print(x)
"""



# 18. Given an array of integers arr[]. Find the Inversion Count in the array.
# Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.
# Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted.
#  If the array is already sorted then the inversion count is 0.
# If an array is sorted in the reverse order then the inversion count is the maximum. 
# Mediam Lavel # Flipkart, Amazon, Microsoft, MakeMyTrip, Adobe, BankBazaar, Myntra

"""
arr = [2, 4, 1, 3, 5]
class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        # Helper function for merge sort and counting inversions
        def merge_and_count(arr, temp_arr, left, right):
            if left == right:
                return 0
            mid = (left + right) // 2
            inv_count = 0
            inv_count += merge_and_count(arr, temp_arr, left, mid)
            inv_count += merge_and_count(arr, temp_arr, mid + 1, right)
            inv_count += merge(arr, temp_arr, left, mid, right)
            return inv_count
        
        # Function to merge two halves and count inversions
        def merge(arr, temp_arr, left, mid, right):
            i = left    # Starting index for left subarray
            j = mid + 1 # Starting index for right subarray
            k = left    # Starting index to be sorted
            inv_count = 0
            
            # Merge the two subarrays while counting inversions
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    temp_arr[k] = arr[j]
                    inv_count += (mid - i + 1)  # All elements left in the left subarray are greater than arr[j]
                    j += 1
                k += 1

            # Copy the remaining elements of left subarray, if any
            while i <= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1

            # Copy the remaining elements of right subarray, if any
            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1

            # Copy the sorted subarray into the original array
            for i in range(left, right + 1):
                arr[i] = temp_arr[i]
            
            return inv_count

        # Create a temporary array for merging
        temp_arr = [0] * len(arr)
        return merge_and_count(arr, temp_arr, 0, len(arr) - 1)

s = Solution()
x = s.inversionCount(arr)
print(x)
"""

# 19. Given an array arr[] that contains positive and negative integers (may contain 0 as well).
# Find the maximum product that we can get in a subarray of arr[].
# Note: It is guaranteed that the output fits in a 32-bit integer.
# Mediam Lavel # Morgan Stanley, Amazon, Microsoft, OYO Rooms, D-E-Shaw Google

"""
arr = [-2, 6, -3, -10, 0, 2]
class Solution:

    def maxProduct(self,arr):

	# Function to find maximum
	# If the array is empty, we cannot compute a product
        if not arr:
            return 0
        
        # Initialize the max and min products as the first element
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]
        
        # Traverse the array starting from the second element
        for i in range(1, len(arr)):
            # If the current element is negative, swap max and min products
            if arr[i] < 0:
                max_product, min_product = min_product, max_product
            
            # Update the max and min products
            max_product = max(arr[i], max_product * arr[i])
            min_product = min(arr[i], min_product * arr[i])
            
            # Update the result to be the maximum of the result so far and max_product
            result = max(result, max_product)
        
        return result


s = Solution()

x = s.maxProduct(arr)
print(x)
"""


# 20. Given an array of integers arr[] in a circular fashion.
# Find the maximum subarray sum that we can get if we assume the array to be circular. 
# Amazon Microsoft
# Hard Level

"""
def circularSubarraySum(arr):
    n = len(arr)
    
    # Case 1: Find the maximum subarray sum using Kadane's algorithm for a non-circular array
    def kadane(arr):
        max_sum = arr[0]
        current_sum = arr[0]
        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    max_kadane = kadane(arr)
    
    # Case 2: Find the minimum subarray sum using Kadane's algorithm (invert signs)
    def kadane_min(arr):
        min_sum = arr[0]
        current_sum = arr[0]
        for i in range(1, len(arr)):
            current_sum = min(arr[i], current_sum + arr[i])
            min_sum = min(min_sum, current_sum)
        return min_sum
    
    min_kadane = kadane_min(arr)
    
    # Case 3: Find the total sum of the array
    total_sum = sum(arr)
    
    # If all elements are negative, then the maximum circular subarray sum is just the maximum subarray sum
    if total_sum == min_kadane:
        return max_kadane
    
    # Return the maximum of the Kadane result or the total_sum - min_kadane (circular sum)
    return max(max_kadane, total_sum - min_kadane)

# Example usage
arr = [8, -8, 9, -9, 10, -11, 12]
print(circularSubarraySum(arr))  # Output will be the maximum circular subarray sum

"""

# 21. Given an array of Intervals arr[][],
# where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.
# Medium Level 
# Microsoft Amazon Google Netflix 

"""
class Solution:
    def mergeOverlap(self, arr):
        # Step 1: Sort the intervals by start time
        arr.sort(key=lambda x: x[0])
        
        # Step 2: Create a result list to store merged intervals
        merged_intervals = []
        
        # Step 3: Iterate through the sorted intervals
        for interval in arr:
            # If merged_intervals is empty or no overlap, add the interval
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                # There is overlap, so merge the current interval
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        
        # Return the merged intervals
        return merged_intervals

# Example usage
sol = Solution()
arr = [[1, 3], [2, 4], [6, 8], [7, 10], [9, 12]]
print(sol.mergeOverlap(arr))  # Output will be [[1, 4], [6, 12]]
"""


# 22. You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.
# Note: Positive number starts from 1. The array can have negative integers too.
# Medium Level
# Accolite, Amazon, Samsung, Snapdeal

"""
class Solution:
    
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Place each number in its correct position.
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                # Swap arr[i] and arr[arr[i] - 1] to put the number in its correct index.
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        
        # Step 2: Find the first index where arr[i] != i + 1
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        # Step 3: If all numbers from 1 to n are present, the missing number is n + 1.
        return n + 1

arr = [3, 4, -1, 1]
solution = Solution()
print(solution.missingNumber(arr))  # Output will be 2

"""

# 23. Geek has an array of non-overlapping intervals intervals where intervals[i] = [starti,
# endi] represent the start and the end of the ith event and intervals is sorted in ascending order by starti.
# He wants to add a new interval newInterval= [newStart, newEnd] where newStart and newEnd represent the start and end of this interval.

# Help Geek to insert newInterval into intervals such that intervals is still sorted in ascending order by starti
# and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Medium Level 

"""
class Solution:
    def insertInterval(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # Step 1: Add all intervals that come before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])  # Update start
            newInterval[1] = max(newInterval[1], intervals[i][1])  # Update end
            i += 1
        
        # Step 3: Add the merged interval
        result.append(newInterval)

        # Step 4: Add all intervals that come after the new interval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
solution = Solution()
print(solution.insertInterval(intervals, newInterval))
"""


# 24. Given a string s, the objective is to convert it into integer format without utilizing any built-in functions.
# Refer the below steps to know about atoi() function.
# Cases for atoi() conversion:

# Skip any leading whitespaces.
# Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
# Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached.
# If no digits are present, return 0.
# If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.
# Medium Level 
# Morgan Stanley, Amazon, Microsoft, Payu, Adobe, Code Brew

"""
class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Skip leading whitespaces
        i = 0
        n = len(s)
        
        # Skip all whitespaces at the beginning
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Handle optional sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        else:
            sign = 1
        
        # Step 3: Read digits
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')  # Convert char to digit
            result = result * 10 + digit
            i += 1
        
        # Step 4: Apply the sign
        result *= sign
        
        # Step 5: Handle overflow/underflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        return result


solution = Solution()

# Test cases
print(solution.myAtoi("42"))               # Output: 42
print(solution.myAtoi("   -42"))           # Output: -42
print(solution.myAtoi("4193 with words"))  # Output: 4193
print(solution.myAtoi("words and 987"))    # Output: 0
print(solution.myAtoi("-91283472332"))     # Output: -2147483648 (overflow)

"""

# 25. Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ].
#  Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#  Medium Level

"""
class Solution:
    def minRemoval(self, intervals):
        # Step 1: Sort intervals based on the end time
        intervals.sort(key=lambda x: x[1])
        
        # Step 2: Initialize variables
        last_end = float('-inf')  # Initially, no interval has been selected
        non_overlap_count = 0  # To count the number of non-overlapping intervals

        # Step 3: Iterate through the sorted intervals
        for interval in intervals:
            # If current interval does not overlap with the last selected one
            if interval[0] >= last_end:
                non_overlap_count += 1  # Select this interval
                last_end = interval[1]  # Update the end time to the current interval's end

        # Step 4: The minimum number of intervals to remove is the total intervals minus non-overlapping intervals
        return len(intervals) - non_overlap_count


solution = Solution()

# Test cases
print(solution.minRemoval([[1,2],[2,3],[3,4],[1,3]]))  # Output: 1
print(solution.minRemoval([[1,2],[1,2],[1,2]]))        # Output: 2
print(solution.minRemoval([[1,2],[2,3]]))              # Output: 0
print(solution.minRemoval([[1,2],[3,4],[5,6],[7,8]]))  # Output: 0

"""

# 26. Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space.
# Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

# Medium Level 
# Zoho, Microsoft, Snapdeal, Goldman Sachs, Adobe, Linkedin, Amdocs, Brocade, Juniper Networks, Quikr, Synopsys

"""
class Solution:
    def mergeArrays(self, a, b):
        # code here
        n = len(a)
        m = len(b)
        
        # Step 1: Start merging by comparing elements from end of a[] and start of b[]
        i = n - 1  # Last index of a[]
        j = 0      # First index of b[]
        
        # Step 2: Merge elements into their correct positions
        while i >= 0 and j < m:
            if a[i] > b[j]:
                # Swap a[i] and b[j]
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
            else:
                break
        
        # Step 3: Sort array a[] to maintain its sorted order
        a.sort()
        
        # Step 4: Sort array b[] to maintain its sorted order
        b.sort()

        return a, b

a = [1, 3, 5, 7] 
b = [0, 2, 6, 8, 9]

c = [1, 2, 3]
d = [5, 8, 9]

s= Solution()
x = s.mergeArrays(a,b)
y = s.mergeArrays(c,d)
print(x)
print(y)
"""
# 27. A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum element in it.
# easy level
# Morgan Stanley, Amazon, Microsoft, Samsung, Snapdeal Adobe, Times Internet 

"""
arr= [5, 6, 1, 2, 3, 4]

class Solution: # Methord 1 Normal Aproach
    def findMin(self, arr):
        #complete the function here
        ar= list(arr)
        ar.sort()
        return ar[0]
s = Solution()
x = s.findMin(arr)
print(x)
"""

"""
class Solution: # Methord 2 binary search
    def findMin(self, arr):
        #complete the function here
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum element is in the right half
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        
        # When left == right, it points to the minimum element
        return arr[left]

s = Solution()
y = s.findMin(arr)
print(y)
"""

#28. Given a sorted and rotated array arr[] of distinct elements,
# the task is to find the index of a target key. Return -1 if the key is not found.
# mediam level
# Paytm, Flipkart, Amazon, Microsoft, Snapdeal, D-E-Shaw, FactSet, Hike, MakeMyTrip, Intuit, Adobe, Google, BankBazaar, Times Internet

"""
class Solution:
    def search(self,arr,key):
        # Complete this function
        
        n = len(arr)
        result =-1
        for i in range(n):
            if arr[i] == key:
                result=i
                
        return result


s= Solution()
x= s.search(arr= [5, 6, 7, 8, 9, 10, 1, 2, 3],key = 3)
y= s.search(arr= [3, 5, 1, 2],key = 6)
print(x)
print(y)
"""


# 29. Given an array arr[] where no two adjacent elements are same, find the index of a peak element.
# An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements,
# return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".
# Note: Consider the element before the first element and the element after the last element to be negative infinity.
# basic Level
# Accolite, Amazon, Visa, Adobe, Google

"""
class Solution:
    def peakElement(self, arr):
        n = len(arr)
        
        # Handle the boundary cases
        if n == 1:  # If there's only one element, it's a peak
            return 0
        if arr[0] > arr[1]:  # First element is a peak
            return 0
        if arr[n-1] > arr[n-2]:  # Last element is a peak
            return n-1
        
        # Check the middle elements
        for i in range(1, n-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:  # Peak condition
                return bool(i)
        
        return bool(-1)  # This line should never be reached if input follows the constraints

arr = [1, 2, 4, 5, 7, 8, 3]
solution = Solution()
index = solution.peakElement(arr)
print(index)  # Expected output: 2, since 20 is greater than both 3 and 4
"""

# 30. You are given an array with unique elements of stalls[], which denote the position of a stall.
#  You are also given an integer k which denotes the number of aggressive cows.
#  Your task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.
#  medium Level

"""
class Solution:
    def aggressiveCows(self, stalls, k):
        # Sort the stalls positions
        stalls.sort()
        
        # Helper function to check if it's possible to place cows with at least 'dist' distance apart
        def canPlaceCows(stalls, k, dist):
            count = 1  # Place the first cow in the first stall
            last_position = stalls[0]  # Position of the first cow
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= dist:  # If the current stall is far enough for the next cow
                    count += 1
                    last_position = stalls[i]  # Update the position of the last placed cow
                    if count == k:  # If all cows are placed
                        return True
            return False
        
        # Binary search on the distance
        low = 1  # Minimum possible distance
        high = stalls[-1] - stalls[0]  # Maximum possible distance
        best_dist = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceCows(stalls, k, mid):
                best_dist = mid  # If we can place cows with this distance, try for a larger distance
                low = mid + 1
            else:
                high = mid - 1
        
        return best_dist


sol = Solution()
stalls = [1, 2, 8, 4, 9]
k = 3
print(sol.aggressiveCows(stalls, k))  # Output: 3
"""

# 30. You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book.
# You also have an integer k representing the number of students. The task is to allocate books to each student such that:

# Each student receives atleast one book.
# Each student is assigned a contiguous sequence of books.
# No book is assigned to more than one student.
# The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations,
# find the arrangement where the student who receives the most pages still has the smallest possible maximum.
# Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).
# Medium Level
# Infosys, Amazon, Microsoft, Google, Codenation, Uber

"""
class Solution:
    
    # Function to find the minimum number of pages.
    def findPages(self, arr, k):
        n = len(arr)
        
        # If there are fewer books than students, allocation is not possible
        if n < k:
            return -1
        
        # Helper function to check if a given max number of pages can be assigned to students
        def canAllocate(arr, k, max_pages):
            student_count = 1  # Start with the first student
            current_sum = 0  # Keep track of the current sum of pages for the student
            
            for pages in arr:
                if current_sum + pages > max_pages:
                    # If adding this book exceeds the max_pages, assign to the next student
                    student_count += 1
                    current_sum = pages
                    
                    # If we exceed the number of students, return False
                    if student_count > k:
                        return False
                else:
                    # Otherwise, add the book to the current student's allocation
                    current_sum += pages
            
            return True
        
        # Binary search to find the minimum possible maximum number of pages
        low = max(arr)  # Lower bound of the maximum pages (at least the largest book)
        high = sum(arr)  # Upper bound of the maximum pages (all books to one student)
        
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if canAllocate(arr, k, mid):
                result = mid  # We can allocate with this max, try for a smaller value
                high = mid - 1
            else:
                low = mid + 1  # We cannot allocate with this max, try a larger value
        
        return result


# Test case
solution = Solution()
arr = [12, 34, 67, 90]  # Pages in the books
k = 2  # Number of students
print(solution.findPages(arr, k))  # Output: 113

"""


# 31 Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number x is present in the matrix or not.
# Note: In a strictly sorted matrix, each row is sorted in strictly increasing order,
# and the first element of the ith row (i!=0) is greater than the last element of the (i-1)th row.
# medium level
# Paytm, Accolite, MakeMyTrip, Ola, Cabs, Oracle, Visa, Goldman, Sachs, Directi, Groupon, InMobi, One97, Polycom, TinyOwl

"""
mat = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
x= 5


class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 
    	# Get the dimensions of the matrix
        n = len(mat)  # Number of rows
        m = len(mat[0])  # Number of columns
        
        # Start from the top-right corner
        i, j = 0, m - 1
        
        # Traverse the matrix
        while i < n and j >= 0:
            if mat[i][j] == x:
                return True  # Number found
            elif mat[i][j] > x:
                j -= 1  # Move left
            else:
                i += 1  # Move down
        
        # If we exit the loop, x is not in the matrix
        return False

s= Solution()
x= s.searchMatrix(mat, x)
print(x)
"""


#32 You are given a 2D matrix mat[][] of size n×m. The task is to modify the matrix such that if mat[i][j] is 0,
# all the elements in the i-th row and j-th column are set to 0 and do it in constant space complexity.
# Medium Level

"""
mat = [[1, -1, 1],
       [-1, 0, 1],
       [1, -1, 1]]

class Solution:
    def setMatrixZeroes(self, mat):
        n, m = len(mat), len(mat[0])
        
        # Flags to check if the first row and first column need to be set to zero
        first_row_zero = any(mat[0][j] == 0 for j in range(m))
        first_col_zero = any(mat[i][0] == 0 for i in range(n))
        
        # Use first row and first column as markers
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0  # Mark row
                    mat[0][j] = 0  # Mark column
        
        # Set the elements to 0 based on the markers in first row and column
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        
        # Handle the first row
        if first_row_zero:
            for j in range(m):
                mat[0][j] = 0
        
        # Handle the first column
        if first_col_zero:
            for i in range(n):
                mat[i][0] = 0
        
        return mat


s= Solution()
x= s.setMatrixZeroes(mat)
print(x)
"""

# 33. Given an array arr[] of positive integers and another integer target.
# Determine if there exists two distinct indices such that the sum of there elements is equals to target.
# Easy Level
# Zoho, Flipkart, Morgan Stanley, Accolite, Amazon, Microsoft, FactSet, Hike, Adobe, Google, Wipro, SAP Labs CarWale

"""
arr = [1, 4, 45, 6, 10, 8]
target = 16


class Solution:
	def twoSum(self, arr, target):
         n = len(arr)
         for i in range(n):
            for j in range(1,n):
                if arr[i]+arr[j]==target:
                    return arr[i],"+",arr[j]," = ",target


s = Solution()
x = s.twoSum(arr, target)
print(x)
"""

# Methord Two 
"""
class Solution:
	def twoSum(self, arr, target):
		# code here
		# Create a dictionary to store the numbers we have already seen
         seen = {}
        
        # Iterate through the array
         for num in arr:
            # Calculate the complement (the number that, when added to 'num', equals the target)
            complement = target - num
            
            # If the complement is in the dictionary, we have found the pair
            if complement in seen:
                return seen[complement], "+", num, "=", target
            
            # Store the current number in the dictionary
            seen[num] = True

s = Solution()
y = s.twoSum(arr, target)
print(y)
"""
