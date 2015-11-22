

def Matrix_Chain_order(p):
    n=len(p)-1
    M=[[0 for y in range(n)]for x in range(n)]
    S=[[0 for y in range(n-2)]for x in range(n-2)]

    for i in range(0,n):
        M[i][i]=0

        print M
    for l in range(2,n+1):
            print l

            for i in range(l,(n-l+1)):

                j=i+l-1

                M[i][j]=pow(2,1024)

                for k in range(i,(j-1)):

                    q=M[i][k]+M[k+1][j]+p[j-1]*p[k]*p[j]
                    print q
                    if q<M[i][j]:
                        M[i][j]=q
                        S[i][j]=k





    return M,S

      #            k best place for cut






def Print_Optimal_Parns(S,i,j):
    if i==j:
       print 'A'
    else:
        print '('
        Print_Optimal_Parns(S,i,S[i][j])
        Print_Optimal_Parns(S,S[i][j]+1,j)
        print ')'

A1=[50][100]
A2=[100][3]
A3=[3][5]
S=[A1,A2,A3]
p=[50,100,3,5]

# S=Matrix_Chain_order(p)
Print_Optimal_Parns(S,1,3)
