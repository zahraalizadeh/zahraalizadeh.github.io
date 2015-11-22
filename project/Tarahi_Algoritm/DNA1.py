
from collections import Counter

def count_letters(words):
    counter = Counter()
    for word in words.split():
        counter.update(word)
    return sum(counter.itervalues())




def DNA(x, y):
    m=count_letters(x)
    n=count_letters(y)
    b=[[]*(m-1)]*(n-1)

    C = [[] * (m+1 )] * (n+1 )
    for i in range(1,m+2):

        C[i][0]=0
        print  1
    for j in range(n+2):
        C[0][j]=0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i]==y[j]:
                C[i][j]=C[i-1][j-1]+1
                b[i][j]='r'
            elif C[i-1][j]>= C[i][j-1]:
                C[i][j]=C[i-1][j]
                b[i][j]='up'
            else:
                C[i][j]=C[i][j-1]
                b[i][j]='es'
    print C,b
    return C,b
def print_Lcp(b,X,i,j):
    if i==0 or j==0:
        return X
    if b[i][j]=='r':
        print_Lcp(b,X,i-1,j-1)
        print X[i]
    elif b[i][j]=='up':
        print_Lcp(b,X,i-1)
    else:
        print_Lcp(b,X,i,j-1)



x="ABCGT"
y="ABCG"
DNA(x,y)
# a=print_Lcp(b[1],b[0],5,4)
# print a