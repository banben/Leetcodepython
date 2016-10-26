class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = list(s)
        n = len(s)
        u = ['a', 'e', 'i', 'o', 'u']
        i = 0
        j = n - 1
        while i < j:
            while i < n and s[i].lower() not in u:
                i += 1
            while j > 0 and s[j].lower() not in u:
                j -= 1
            if i >= j:
                break
            ans[j] = s[i]
            ans[i] = s[j]
            i += 1
            j -= 1
        return ''.join(ans)
