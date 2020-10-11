import numpy as np
class MyClass():
    def Progression(b,q,n):
        a= np.zeros(shape=[n])
        i=0
        while(i<n):
            b*=q
            i+=1
            a[i-1]=b
        return a
    def Return_k(b,q,n,a,k):
        ku=0
        i=0
        while(i<n):
            b*=q
            if(i<k)&(k<n):
                ku+=b
            i+=1
            a[i-1]=b
        return(ku)
    def presenceElement(j,a):
        if (j in a):
           print ('True')
        else:
           print ('False')

        return (j in a)
    def elemReturn(c,a):
        print(a[c])
        return a[c] 

