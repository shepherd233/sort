def sort(A,B):
    c=[]
    i,j=0,0
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            c.append(A[i])
            i+=1
        else:
            c.append(B[j])
            j+=1
    if i==len(A):
        c+=B[j:]
    if j==len(B):
        c+=A[i:]
    return c
def mergeSort(A):
    n=len(A)
    if n<2:
        return A
    left=mergeSort(A[:n//2])
    right=mergeSort(A[n//2:])
    return sort(left,right)
if __name__=="__main__":
    a=[7,5,6,2,9,1,0,3,4,10]
    print(a)
    print(mergeSort(a))