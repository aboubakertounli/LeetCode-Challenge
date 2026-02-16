class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
# Example usage:

solution = Solution()
s = "abcabcbb"
result = solution.lengthOfLongestSubstring(s)
print(result)  # Output: 3 (the longest substring is "abc")
s = "bbbbb"
result = solution.lengthOfLongestSubstring(s)
print(result)  # Output: 1 (the longest substring is "b")
s = "pwwkew"
result = solution.lengthOfLongestSubstring(s)
print(result)  # Output: 3 (the longest substring is "wke")