def Optimal_BST(p,q,n):

  e=[[]*n]*n
  w=[[]*n]*n
  Root=[[]*n]*n
  for i in range(1,n+2):
      e[i][i-1]=q[i]-1
      w[i][i-1]=q[i]-1
  for l in range(1,n+1):
      for i in range(l,n-l+2):
          j=i-l+1
          e[i][j]=pow(2,11)
          w[i][j]=w[i][j-1]+p[j]+q[j]
          for r in range(i,j+1):
              a=e[i][r-1]+e[r+1][j]+w[i][j]
              if a<e[i][j]:
                  e[i][j]=a
                  Root[i][j]=r


  return e ,Root

p=[0,0.15,0.10,0.05,0.10,0.20]
q=[0.05,0.10,0.05,0.05,0.05,0.10]
a=Optimal_BST(p,q,4)
print a