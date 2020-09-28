"""
Use "Sliding Window" Algorithm to solve this

Set two pointers, i and j, to 0
This two pointers will be used as windows frames, j is the left one and i is the right one
Then set max_count to 0
This variable will be updated every loop tick with the formula: i-j+1. This will yield the lenght of the actual set
Then loop over with a while till i pointer is less than the length of the string
Inside the loop:
While the char of the pointer in i is inside the set:
    Remove the j pointing character inside the set
    increase j by one
add the i pointer character to the set
calculate the max count with i-j+1
increase i by one
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        i,j,max_count,sub = 0,0,0,set()
        while i<len(s):
            while s[i] in sub:
                sub.remove(s[j])
                j+=1
            sub.add(s[i])
            max_count = max(max_count,i-j+1)
            i+=1
        return max_count

        
#Test the solution
sol = Solution()
res = sol.lengthOfLongestSubstring("abcabcbb")
print(res)
res = sol.lengthOfLongestSubstring("bbbbb")
print(res)
res = sol.lengthOfLongestSubstring("pwwkew")
print(res)