class Solution:
    def longestCommonPrefix(self, strs: str) -> str:
        strs = ["flower","flow","flight"]
        prefix = strs[0][0]
        for i in range(len(strs)):
            for j in range(len(prefix)):
                if strs[i][j] != prefix[j]:
                    prefix.pop(prefix[j])
        return prefix
    