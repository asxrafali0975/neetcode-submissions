class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])

        lr = 0
        hr = row-1

        

        while lr <= hr:
            mid_row = (lr+hr)//2
            if target >= matrix[mid_row][0] and target<=matrix[mid_row][col-1]:
                lc = 0
                hc = col-1

                while lc<=hc:
                    mid_col = (lc+hc)//2
                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] > target:
                        hc = mid_col-1
                    else:
                        lc = mid_col+1
                return False

            elif target < matrix[mid_row][0]:
                hr = mid_row-1

            else:
                lr = mid_row+1
                 
        return False


