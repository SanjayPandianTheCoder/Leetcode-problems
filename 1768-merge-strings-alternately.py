class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combinedStr = ''
        len1 = len(word1)
        len2 = len(word2)

        index = 0
        while(index<len1 and index<len2):
            combinedStr += word1[index] + word2[index]
            index += 1
        while(index<len1):
            combinedStr += word1[index]
            index += 1
        while(index<len2):
            combinedStr += word2[index]
            index += 1
        print (combinedStr)
        return combinedStr