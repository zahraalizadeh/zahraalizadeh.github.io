# maximum hazine
def Bottom_Up_Cut_Rod(p,n):

   r=[-1]*(n+1)
   r[0]=0
   j=1

   while j<=n:
       q=0
       i=1
       while i<=j:
           q=max(q,p[i-1]+r[j-i])

           i+=1
       r[j]=q
       j+=1

   return r
# avalin boreshhayeh monaseb
def Extend_Bottom_up_Cut_Rod(p,n):



    s=[-1]*(n+1)
    s[0]=0
    r=Bottom_Up_Cut_Rod(p,n)
    r[0]=0
    j=1
    while j<=n:
        q=0
        i=1
        while i<=j:
            if q<p[i-1]+r[j-i]:
                q=p[i-1]+r[j-i]
                s[j]=i

            r[j]=q

            i+=1


        j+=1

    print r
    return s


def PRINT_Cut_Rod (p,n):

 s=Extend_Bottom_up_Cut_Rod(p,n)
 print s




 while n>0:
    print s[n]
    n=n-s[n]


p=[1,5,8,9,10,17,17,20,24,30]
PRINT_Cut_Rod(p,7)