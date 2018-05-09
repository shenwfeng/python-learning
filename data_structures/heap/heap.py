import math
'''
堆（英语：heap)是计算机科学中一类特殊的数据结构的统称。堆通常是一个可以被看做一棵树的数组对象。

堆的定义：
     堆（英语：heap)是计算机科学中一类特殊的数据结构的统称。堆通常是一个可以被看做一棵树的数组对象。

    堆总是满足下列性质：
           堆中某个节点的值总是不大于或不小于其父节点的值；
           堆总是一棵完全二叉树。

    将根节点最大的堆叫做最大堆或大根堆，根节点最小的堆叫做最小堆或小根堆。常见的堆有二叉堆、斐波那契堆等。
    堆的定义如下：n个元素的序列{k1,k2,ki,…,kn}当且仅当满足下关系时，称之为堆。
     (ki <= k2i,ki <= k2i+1)或者(ki >= k2i,ki >= k2i+1), (i = 1,2,3,4...n/2)

       若将和此次序列对应的一维数组（即以一维数组作此序列的存储结构）看成是一个完全二叉树，则堆的含义表明，
    完全二叉树中所有非终端结点的值均不大于（或不小于）其左、右孩子结点的值。由此，若序列{k1,k2,…,kn}是堆，
    则堆顶元素（或完全二叉树的根）必为序列中n个元素的最小值（或最大值）。

    堆支持以下的基本:
       build:建立一个空堆；
       insert:向堆中插入一个新元素；
       update：将新元素提升使其符合堆的性质；
       get：获取当前堆顶元素的值,
       delete：删除堆顶元素；需要弹出堆顶的元素，并再次使其成为一个堆
       heapify：使删除堆顶元素的堆再次成为堆。

       某些堆实现还支持其他的一些操作，如斐波那契堆支持检查一个堆中是否存在某个元素。

'''


class Heap(object):
    def __init__(self):
        self.heap = []
        self.currsize = 0

    def buildHeap(self,a):
        self.heap = list(a)
        self.currsize = len(a)
        for i in range(self.currsize//2-1,-1,-1):
            self.maxHeapify(i)


    #获取i节点的左孩子的下标，没有返回None
    def leftChild(self,i):
        if 2*i+1< self.currsize:
            return 2*i+1
        return None
    #获取i节点的右孩子的下标，没有返回None
    def rightChild(self,i):
        if 2*i+2< self.currsize:
            return 2*i+2
        return None

    #获取i节点的父节点，没有返回None，i为从0开始的自然数
    def getParent(self,i):
        # if i < self.currsize:
        #     if i==0:
        #         return 0
        #     else:
        #         if i//2 == i/2:
        #             return i//2-1
        #         return i//2
        # return None
        if i < self.currsize:
            if i==0:
                return 0
            return (i-1)//2

    def maxHeapify(self,i):
        # #常规算法，可能需要四次移动数据，平均需要两次，此种方法有缺陷，没有办法解决调换数据后引起的联动问题。
        # if i<self.currsize:
        #     lc = self.leftChild(i)
        #     rc = self.rightChild(i)
        #     if (lc is not None) and (self.heap[i]< self.heap[lc]):
        #         temp = self.heap[i]
        #         self.heap[i] = self.heap[lc]
        #         self.heap[lc] = temp
        #     if (rc is not None) and (self.heap[i]<self.heap[rc]):
        #         temp = self.heap[i]
        #         self.heap[i] = self.heap[rc]
        #         self.heap[rc] = temp

        #优化的算法，尽量减少数据的移动，同时解决联动问题，这个对于现有heap 删除一个数据后自动生成一个heap
        if i<self.currsize:
            m = i
            lc = self.leftChild(i)
            rc = self.rightChild(i)
            if (lc is not None) and (self.heap[i]<self.heap[lc]):
                m = lc
            if (rc is not None) and (self.heap[m]<self.heap[rc]):
                m = rc
            if m != i:
                temp = self.heap[i]
                self.heap[i]=self.heap[m]
                self.heap[m] = temp
                #必须要有这个可以通过联动的方法，解决数据变动后的后续问题
                self.maxHeapify(m)








    #大根堆
    def insert(self,data):
        self.heap.append(data)
        curr = self.currsize
        self.currsize += 1
        while self.heap[curr] > self.heap[self.getParent(curr)]:
            temp = self.heap[curr]
            self.heap[curr] = self.heap[self.getParent(curr)]
            self.heap[self.getParent(curr)] = temp
            curr = self.getParent(curr)

    def display(self):
        print(self.heap)
        print(self.currsize)




t = Heap()
l = [1,6,4,8,7,6,5,13,12,11,5,20]
print(l)
t.buildHeap(l)
# h.maxHeapify(0)
h =Heap()
h.insert(1)
h.insert(6)
h.insert(4)
h.insert(8)
h.insert(7)
h.insert(6)
h.insert(5)
h.insert(13)
h.insert(12)
h.insert(11)
h.display()
h.insert(5)
h.insert(20)
t.display()
print("----------------")
h.display()