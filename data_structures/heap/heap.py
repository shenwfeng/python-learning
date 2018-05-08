'''
堆（英语：heap)是计算机科学中一类特殊的数据结构的统称。堆通常是一个可以被看做一棵树的数组对象。堆总是满足下列性质：

    堆中某个节点的值总是不大于或不小于其父节点的值；
    堆总是一棵完全二叉树。

将根节点最大的堆叫做最大堆或大根堆，根节点最小的堆叫做最小堆或小根堆。常见的堆有二叉堆、斐波那契堆等。
堆的定义如下：n个元素的序列{k1,k2,ki,…,kn}当且仅当满足下关系时，称之为堆。
(ki <= k2i,ki <= k2i+1)或者(ki >= k2i,ki >= k2i+1), (i = 1,2,3,4...n/2)

若将和此次序列对应的一维数组（即以一维数组作此序列的存储结构）看成是一个完全二叉树，
则堆的含义表明，完全二叉树中所有非终端结点的值均不大于（或不小于）其左、右孩子结点的值。
由此，若序列{k1,k2,…,kn}是堆，则堆顶元素（或完全二叉树的根）必为序列中n个元素的最小值（或最大值）。
'''



'''
    build:建立一个空堆；
    insert:向堆中插入一个新元素；
    update：将新元素提升使其符合堆的性质；
    get：获取当前堆顶元素的值；
    delete：删除堆顶元素；
    heapify：使删除堆顶元素的堆再次成为堆。

某些堆实现还支持其他的一些操作，如斐波那契堆支持检查一个堆中是否存在某个元素。

'''

class Heap(object):
    def __init__(self):
        self.heap = []
        self.size = 0

    def empty(self):
        if self.size == 0:
            return True
        return False

    def getParent(self,i):
        if i<= self.size:
            return i//2
        return None

    def getLeft(self,i):
        if 2*i+1 <= self.size:
            return 2*i+1
        return None

    def getRight(self,i):
        if 2*i+2<=self.size:
            return 2*i+2
        return None

    def insert(self,data):
        self.size += self.size
        self.heap.append(data)
        i = self.size-1
        while  data > self.heap[self.getParent(i)]:
            self.heap[i],self.heap[self.getParent(i)]=self.heap[i],self.heap[self.getParent(i)]
            i = self.getParent(i)

    def display(self):
        print(self.heap)







h = Heap()
h.insert(0)
h.insert(1)
h.insert(10)
h.insert(8)
h.insert(9)
h.insert(2)
h.display()




