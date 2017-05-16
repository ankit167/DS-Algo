#!/usr/bin/python


# Design a special stack where push(), pop(), getMin(), isEmpty(), isFull()
# take T(n)- O(1)
class SpecialStack:
    realStack = []
    auxStack = []
    top = -1

    def __init__(self, size):
        self.size = size

    def isFull(self):
        if self.top == self.size-1:
            print 'Stack is Full'
            return True
        return False

    def isEmpty(self):
        if self.top == -1:
            print 'Stack is Empty'
            return True
        return False

    def push(self, data):
        if self.isFull():
            return
        self.realStack.append(data)
        self.top += 1
        if len(self.auxStack) == 0 or data <= self.auxStack[-1]:
            self.auxStack.append(data)

    def pop(self):
        if self.isEmpty():
            return
        element = self.realStack.pop()
        self.top -= 1
        print 'Popped Element- %s' % element
        if len(self.auxStack) > 0 and element == self.auxStack[-1]:
            self.auxStack.pop()

    # T(n) = O(1)
    def getMin(self):
        if len(self.auxStack) == 0:
            return
        print self.auxStack[-1]


def main():
    s = SpecialStack(5)
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(10)
    s.push(40)
    s.push(50)
    s.pop()
    s.getMin()
    s.push(5)
    s.getMin()
    s.pop()
    s.pop()
    s.getMin()

if __name__ == '__main__':
    main()
