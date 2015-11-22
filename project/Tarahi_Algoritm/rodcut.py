__author__ = 'alizadeh'
def Cut_Rod(p,n):

   r=[-1]*(n+1)
   r[0]=0


   return MEMOIZED_cut_rod(p,n,r)

def MEMOIZED_cut_rod(p,n,r):
    if r[n]>=0:
        return r[n]
    if n==0:
        q=0

    else:

        q=0
        i=1
        while i<=n:
            q=max(q,p[i-1]+MEMOIZED_cut_rod(p,n-i,r))
            i+=1
    r[n]=q

    return q

p=[1,5,8,9,10,17,17,20,24,30]

a=Cut_Rod(p,7)
print a