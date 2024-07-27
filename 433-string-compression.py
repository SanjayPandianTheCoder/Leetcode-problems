class Solution:
    def compress(self, chars: List[str]) -> int:
        resultList = []
        visit = set('1')
        index = 0
        
        while len(chars) > 0:
            resultList.append(chars[0])
            count = 0
            curr_char = chars[0]
            while len(chars) > 0 and chars[0] == curr_char:
                count += 1
                chars.pop(0)
            count = str(count)
            if len(count)>1:
                for c in count:
                    resultList.append(c)
            elif count == '1':
                pass
            else:
                resultList.append(count)
            # print(chars, resultList, count)
            count = 0
        
        for char in resultList:
            chars.append(char) 
        return len(chars)
            