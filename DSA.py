
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
