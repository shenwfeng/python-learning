class Node(object):
    def __init__(self,data,parent,left=None,right=None,):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def setData(self,data):
        self.data = data

    def setLeft(self,left):
        self.left = left

    def setRight(self,right):
        self.right = right

    def setParent(self,parent):
        self.parent = parent

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def empty(self):
        if self.root is None:
            return True
        return False

    def getRoot(self):
        return self.root

    def insert(self,data):
        new_node = Node(data,None)
        if self.empty():
            self.root = new_node
        else:
            cur_node = self.root
            while cur_node is not None:
                par_node = cur_node
                if new_node.getData()< cur_node.getData():
                    cur_node  = par_node.getLeft()
                else:
                    cur_node = par_node.getRight()
            if new_node.getData()< par_node.getData():
                par_node.setLeft(new_node)
            else:
                par_node.setRight(new_node)
            new_node.setParent(par_node)

    def getNode(self,data):
        cur_node = None
        if not self.empty():
            cur_node = self.root
            while (cur_node is not None) and (cur_node.getData() is not data):
                if data < cur_node.getData():
                    cur_node = cur_node.getLeft()
                else:
                    cur_node = cur_node.getRight()
        return cur_node
    """
    取二叉树中某个节点下最大值，默认从二叉搜索树根开始查找
    """
    def getMax(self,root=None):
        if (root is not None):
            cur_node = root
        else:
            cur_node = self.getRoot()
        if (not self.empty()):
            while(cur_node.getRight() is not None):
                cur_node = cur_node.getRight()
        return cur_node

    def getMin(self,root=None):
        if (root is not None):
            cur_node = root
        else:
            cur_node = self.getRoot()
        if (not self.empty()):
            while (cur_node.getLeft() is not None):
                cur_node = cur_node.getLeft()
        return cur_node


    def traversal(self):
        list = []
        if not self.empty():
            cur_node = self.root
            return  self.__InOrderTraversal(cur_node)


    '''
    中序遍历二叉树，返回节点的地址列表,   
    '''
    def __InOrderTraversal(self,cur_node):
        nodelist = []
        if cur_node is not None:
            nodelist = nodelist + self.__InOrderTraversal(cur_node.getLeft())
            nodelist.append(cur_node)
            nodelist = nodelist +  self.__InOrderTraversal(cur_node.getRight())
        return nodelist

    def __PreOrderTraversal(self,cur_node):
        nodelist = []
        if cur_node is not None:
            nodelist.append(cur_node)
            nodelist = nodelist + self.__PreOrderTraversal(cur_node.getLeft())
            nodelist = nodelist + self.__PreOrderTraversal(cur_node.getRight())
        return nodelist

    def __PostOrderTraversal(self,cur_node):
        nodelist = []
        if cur_node is not None:
            nodelist.append(cur_node)
            nodelist = nodelist + self.__PostOrderTraversal(cur_node.getLeft())
            nodelist = nodelist + self.__PostOrderTraversal(cur_node.getRight())
        return nodelist

    def PreTraversal(self):
        stack = []
        result = []
        if self.empty() is not None:
            cur_node = self.getRoot()
            stack.append(cur_node)
            while  stack:
                while (cur_node is not None):
                    result.append(cur_node.getData())
                    stack.append(cur_node)
                    cur_node = cur_node.getLeft()
                cur_node = stack.pop().getRight()
        return result


    def InTraversal(self):
        stack = []
        result = []
        if self.empty() is not None:
            cur_node = self.getRoot()
            # stack.append(cur_node)
            while stack or cur_node:
                while cur_node is not None:
                    stack.append(cur_node)
                    cur_node = cur_node.getLeft()
                node = stack.pop()
                result.append(node.getData())
                cur_node = node.getRight()
        return result

    def display(self,order=None):
        if order is None:
            result = self.InTraversal()
            for i in result:
                print(i)
        else:
            pass























#
# n1 = Node(1,None)
# n2 = Node(2,None)
# n3 = Node(3,None)
#
# n1.setLeft(n2)
# n1.setRight(n3)
# n2.setParent(n1)
# n3.setParent(n1)
#
#
# print(n1)
# print(n1.left)
# print(n1.right)
# data = n3.getParent()
# print(data)

t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(5)
t.insert(2)
t.insert(4)
t.insert(9)
t.insert(1)
t.insert(7)
t.insert(6)
t.insert(0)
t.insert(10)
t.insert(19)
t.insert(-6)
t.insert(3)
# n7 = t.getNode(9)
# print(t.getRoot())
# print(t.getRoot().getLeft().getLeft())
# print(t.getRoot().getLeft().getLeft().getRight())
# print(t.getRoot().getLeft().getRight())
# print(t.getRoot().getRight())
# print(n7)
# print(t.getMax().getData())
# print("---------------------")
# print(t.getMin().getData())
# print("---------------------")

list = t.InTraversal()
t.display()

