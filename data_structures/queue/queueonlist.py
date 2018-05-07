class Queue(object):
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def __str__(self):
        printed = '<'+str(self.entries)[1:-1]+'>'
        return printed

    def put(self,item):
        self.entries.append(item)
        self.length += 1

    def get(self):
        self.length -= 1
        dequeued = self.entries[self.front]
        self.front = 1
        self.entries = self.entries[self.front:]
        self.front = 0
        return dequeued

    def rotate(self,rotation):
        for i in range(rotation):
            self.put(self.get())

    def front(self):
        return self.entries[0]

    def size(self):
        return self.length



