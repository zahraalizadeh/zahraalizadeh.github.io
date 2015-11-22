__author__ = 'alizadeh'
def pivot(a, p, q):
    pi = a[p]
    j = q
    i = p + 1
    while (i < j):
        while (i < j and a[j]>pi):
            j-=1
        while (i < j and a[i]<pi):
            i+=1
        if (i<j):
            swap(a,i,j)

    if pi>a[i]:
        swap(a,i,p)
        return i
    else:
        return p

def swap(a, s1, s2):
    # for k in list:
        temp =a[s1]
        a[s1] = a[s2]
        a[s2] = temp
        return (a, s1, s2)
def i_th(a,p,q,i):
    r=pivot(a,p,q)
    if(r==i):
        return a[r]
    elif i<r:
        i_th(a,p,r-1,i)
    else:
        i_th(a,r+1,q,i-(r-p+1))

a=[5,7,2,1,8]

print(i_th(a,0,len(a)-1,2))



