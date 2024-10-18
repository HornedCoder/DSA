'''
Ques:   2D Matrix is given.
        Each cell has a cost associated with it
        for accessing it.
        We need to start from (0,0) cell and go till
        (n-1,n-1) cell.
        We can go only to right or down cell from current cell.
        Find a way in which the cost is minimum.
'''

def MCLC(mat, right_index, down_index):
    if right_index == -1 or down_index == -1:
        return float('inf')
    elif right_index == 0 and down_index == 0:
        return mat[0][0]

    else:
        op1 = MCLC(mat,right_index-1,down_index)
        op2 = MCLC(mat,right_index,down_index-1)
        return mat[right_index][down_index] + min(op1,op2)

twoD =  [[4,7,8,6,4],
        [6,7,3,9,2],
        [3,8,1,2,4],
        [7,1,7,3,7],
        [2,9,8,9,3]]

print(MCLC(twoD,len(twoD)-1,len(twoD)-1))
