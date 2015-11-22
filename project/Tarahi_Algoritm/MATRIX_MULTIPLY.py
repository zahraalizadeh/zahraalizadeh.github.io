def MATIRIX_MULTIPY(Matrix1,Matrix2):
    p=q=0
    for i in range(len(Matrix1[0])):
        p+=1
    for j in range(len(Matrix2)):
        q+=1

    if p is not q:
        print "not equal number columns of matrix1 and row of matrix2 "
    else:
        w=v=0
        for i in range(len(Matrix1)):
         w+=1
        for j in range(len(Matrix2[0])):
         v+=1
        # print w,v
        # Matrix_r= 2*[[0]*3]

        Matrix_r=[[0 for y in xrange(v)] for x in xrange(w)]

        for i in range(len(Matrix1)):
            for j in range(len(Matrix2[0])):
                Matrix_r[i][j]=0
                for k in range(len(Matrix1[0])):
                    Matrix_r[i][j]=Matrix_r[i][j]+Matrix1[i][k]*Matrix2[k][j]
        # return Matrix_r

        print Matrix_r

Matrix1 =([[ 5, 1 ,3,2,5], [ 1, 1,1,1,1]])
Matrix2 =([[3,2,5],[3,2,5],[ 1,0,1], [ 1,2, 1],[2,1,1]])

MATIRIX_MULTIPY(Matrix1,Matrix2)

# Matrix2 = [[0 for y in xrange(3)] for x in xrange(2)]
