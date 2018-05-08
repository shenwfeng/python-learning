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

    '''
    二叉搜素树的插入规则：
    1.检查树是否为空，如为空直接在根节点插入
       2.否则，从根逐层检索，如果值小于根放在推入左边节点，否则推入右边节点。直到找到一个左或右节点
       为空的节点，放到到那里
    '''
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

    def getNode(self,data,root=None):
        if root is None:
            root = self.getRoot()
        cur_node = None
        if not self.empty():
            cur_node = root
            while (cur_node is not None) and (cur_node.getData() != data):
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

    '''
    二叉搜索树的删除，分为三种情况：
        1.删除的节点是树叶：直接删除该节点，先判断该节点是父节点的左点还是右节点，
    直接将其父节点的左（右）节点的值设置为None
    
        2.删除的节点只有左（右）节点：先判断该节点是父节点的左点还是右节点，
    直接修改父节点的左（右）值为其子节点，子节点parent值为父节点
        
        3.删除的节点有左右节点，取此节点右子树的最小值节点的值，将此节点的值赋值为此值，
    然后删除此最小节点（递归操作）
    
    需要考虑的问题：
        4.如果一个BST中有相同值得节点，需要删除此节点时，如何解决？ 
    解决方法函数中设置一个参数root,默认为Ｎone
    
    '''


    def delete(self,data,root=None):
        #获取要删除的节点地址
        if root is None:
            root = self.getRoot()
        node = self.getNode(data,root)
        #
        if node is not None:
            left = node.getLeft()
            right = node.getRight()
            par = node.getParent()
            if not left and not right:
                if data < par.getData():
                    par.setLeft(None)
                else:
                    par.getRight(None)
            elif left and right:
                min = self.getMin(right)
                mindata = min.getData()
                if data == mindata:
                    min = self.getMin(min)
                self.delete(mindata,min)
                node.setData(mindata)
            else:
                if data < par.getData():
                    if right is None:
                        node.getLeft().setParent(par)
                        par.setLeft(left)
                    else:
                        node.getRight().setParent(par)
                        par.setLeft(right)
                else:
                    if right is None:
                        node.getLeft().setParent(par)
                        par.setRight(left)
                    else:
                        node.getRight().setParent(par)
                        par.setRight(right)





    def traversal(self):
        list = []
        if not self.empty():
            cur_node = self.root
            return self.__InOrderTraversal(cur_node)


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



t.display()
t.delete(8)
t.delete(3)
t.delete(3)

print("------------------")
t.display()

