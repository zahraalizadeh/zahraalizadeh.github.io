__author__ = 'Administrator'
# #def prime(n1,n2):
#     #plist=[]
#     #n=n1
#     while n<=n2:
#         flag=True
#         nlist=range(int((n/2)))[2:]
#
#         for i in nlist:
#             if n%i==0:
#                 flag=False
#                 break
#         if flag==True:
#             plist.append(n)
#         n+=1
#     return plist
# if __name__=='__main__':
#      plist=prime(50,950)
#      for p in plist:
#          print p
#
#



def Reverse(n):
     list=[]
    # l =klist[0:]
     while n!=0:
         #klist=range(n%10)
        list.append(n%10)
        n=int(n/10)
     n2=0
     for i in list:
             n2=n2*10+i
     return n2
if __name__=='__main__':
    n=Reverse(128)
    print n

