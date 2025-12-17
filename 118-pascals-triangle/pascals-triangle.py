class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p_tri = [[1]]
        for i in range(1,numRows):
            row = []
            for j in range(i+1):
                if j!= 0 and j!=i: 
                    row.append(p_tri[i-1][j-1]+p_tri[i-1][j])
                else:
                    row.append(1) 
            p_tri.append(row)
        return p_tri


        