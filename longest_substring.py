class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        e = set()
        i = 0
        j = 0
        res = 0
        while i < n and j < n:
            if s[i] not in e:
                e.add(s[i])
                i += 1
                res = max(res, len(e))
            else:
                e.remove(s[j])
                j += 1
        return res


print(Solution().lengthOfLongestSubstring('abcabcbb'))
