class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r=[]
        l=list(s)
        for i in range(len(s)) :
                m=l.pop(i)
                if m in l:
                    r.append(m)
        print(r)
        return len("".join(r))
# Example usage:
solution = Solution()

s = "abcabcbb"
result = solution.lengthOfLongestSubstring(s)
print(result)  # Output: 3
s = "bbbbb"
result = solution.lengthOfLongestSubstring(s)
print(result)  # Output: 1
s = "pwwkew"
result = solution.lengthOfLongestSubstring(s)
print(result)  # Output: 3
