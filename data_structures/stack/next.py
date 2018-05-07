'''
找出序列中后面比当前数大的数，没有返回-1

'''

def printNGE(arr):

    for i in range(0,len(arr),1):
        next = -1
        for j in range(i+1,len(arr),1):
            if arr[i]<arr[j]:
                next = arr[j]
                break
        print(str(arr[i]),'--',str(next))

arr = [11,8,9,13,21,3,5]
printNGE(arr)