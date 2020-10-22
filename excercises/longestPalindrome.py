"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
A palindrome is a string which reads the same in both directions

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        print('->',s)
        return self.getPalindrome(s)
    
    def getPalindrome(self,s:str)->str:
        half = len(s)//2
        if half < 1:
            return s
        res = len(s)%2
        h1 = s[:half:1]
        h2 = s[:half+res-1: -1]

        if h1==h2:
            # print('PALINDROMO',s,'(',res,')',len(s))
            return s
        i=0
        j=len(s)-1
        sss= set()
        while i<len(s) and j<=len(s):
            sss.add(self.getPalindrome(s[i:j:1]))
            j+=1
            i+=1
        return max(sss)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return res

        
"""babad
        res         ""  "b" "b" 
        resLen      1   1   1  
        i           0   0   1
            l       0   -1  1   -1 
            r       0   1   1   2  
            len(s)          5
            s[l]    b       a   d
            s[r]    b       a   b
            (r-l+1) 1       1   4
"""

sol = Solution()
# for pal in ['babad','cbbd','redivider', 'onallano','deified', 'civic', 'radar', 'level', 'rotor', 'kayak', 'reviver', 'racecar', 'madam', 'refer']:
#    print(sol.longestPalindrome(pal))
print(sol.longestPalindrome('babad'))  
# print(sol.longestPalindrome('cbbd'))        