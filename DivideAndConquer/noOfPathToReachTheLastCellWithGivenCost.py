'''
Ques:   2D Matrix is given
        Each cell has a cost associated with it
        for accessing it.
        We need to start from (0,0) cell and go till
        (n-1,n-1) cell.
        We can go only right or down cell from 
        current cell.
        Find the number of ways to reach end of matrix 
        with given total cost
'''

def LC(mat,row,col,cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if mat[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return LC(mat,0,col-1,cost-mat[row][col])
    elif col == 0:
        return LC(mat,row-1,0,cost-mat[row][col])
    else:
        op1 = LC(mat,row-1,col,cost-mat[row][col])
        op2 = LC(mat,row,col-1,cost-mat[row][col])
        return op1+op2
    
twoD =  [[4,7,1,6],
        [5,7,3,9],
        [3,2,1,2],
        [7,1,6,3],
        ]

print(LC(twoD,3,3,25))