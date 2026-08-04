class Solution(object):
    def transpose(self, matrix):
        result=[]
        rows=len(matrix)
        cols=len(matrix[0])

        for col in range(cols):
            new_row=[]
            for row in range(rows):
                new_row.append(matrix[row][col])
            result.append(new_row)

        return result