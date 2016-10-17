class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        for i in range(n):
        	m = len(words[i])
        	c = 0
        	for j in range(n):
        		if len(words[j]) < i + 1:
        			break
        		c += 1
        	if c != m:
        		return False
        	for j in range(m):
        		if words[i][j] != words[j][i]:
        			return False
        return True

s = Solution()
words = [
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
print s.validWordSquare(words)