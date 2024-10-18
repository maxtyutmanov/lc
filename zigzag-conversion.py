class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return self._convert_fast(s, numRows)
        
    def _convert_fast(self, s: str, numRows: int) -> str:
        # source: PAYPALISHIRING, numRows=3
        
        # P   A   H   N
        # A P L S I I G
        # Y   I   R

        if numRows == 1:
            return s
        
        # indexes of rows for numRows=3 be like:
        # 0 1 2 1 0 1 2 1 0
        # or for numRows=4:
        # 0 1 2 3 2 1 0 1 2 3 2 1 0
        
        i = 0
        row_i = 0
        delta = 1
        result = [""] * numRows
        while i < len(s):
            if row_i == numRows - 1:
                delta = -1
            elif row_i == 0:
                delta = 1
            result[row_i] += s[i]
            row_i += delta
            i += 1

        return "".join(result)