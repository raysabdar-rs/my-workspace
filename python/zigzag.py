# Given a string and number of rows, write the string in a zigzag
# columnar pattern. e.g. 
# Input: s = "PAYPALISHIRING", numRows = 3 Output: "PAHNAPLSIIGYIR"
# P   A   H   N
# A P L S I I G
# Y   I   R
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = []
        for n in range(numRows):
            rows.append([])

        i = 0
        dir = True
        for c in s:

            rows[i].append(c)
            if dir:
                if i < numRows - 1:
                    i += 1
                else:
                    dir = False
                    i -= 1
            else:
                if i > 0:
                    i -= 1
                else:
                    dir = True
                    i += 1

        #print(rows)
    
        return ''.join([''.join(rows[i]) for i in range(numRows)])

        
