class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr =[]
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.arr:
            self.arr.append(x)
            self.min.append(x)
        else:
            self.arr.append(x)
            if x< self.min[-1]:
                self.min.append(x)
            else:
                t =self.min.pop(-1)
                self.min.append(x)
                self.min.append(t)
                
    def pop(self):
        """
        :rtype: void
        """
        if not self.arr:
            return -1
        else:
            t =self.arr.pop(-1)
            self.min.remove(t)

    def top(self):
        """
        :rtype: int
        """
        if not self.arr:
            return -1
        else:
            return self.arr[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()