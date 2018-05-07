class Stack(object):
    def __init__(self):
        self.stack = []
        self.top = 0

    def is_empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def push(self,item):
        if self.top < len(self.stack):
            self.stack[self.top] = item
        else:
            self.stack.append(item)

        self.top +=1

    def pop(self):
        if self.is_empty():
            return None
        else:
            self.top -= 1
            return self.stack[self.top]

