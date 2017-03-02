class Stack:

    def __init__(self):
        self.st = []

    def push(self,data):
        self.st.append(data)

    def pop(self):
        if len(self.st) <= 0:
            return
        return self.st.pop()

    #
    # Checks whether stack is empty
    #
    def isEmpty(self):
        return len(self.st) == 0

    #
    # Prints the elements starting from the top of the stack
    #
    def printStack(self):
        if self.isEmpty():
            return
        data = self.pop()
        print data
        self.printStack()
        self.push(data)

    #
    # Inserts data at the bottom of the stack
    #
    def insertBottom(self, data):
        if self.isEmpty():
            self.push(data)
        else:
            d = self.pop()
            self.insertBottom(data)
            self.push(d)

    #
    # Reverses a stack recursively
    #
    def reverseStack(self):
        if self.isEmpty():
            return
        data = self.pop()
        self.reverseStack()
        self.insertBottom(data)



def main():
    s = Stack()
    l = list(raw_input().split())
    for i in l:
        s.push(i)
    s.reverseStack()
    s.printStack()


if __name__ == "__main__":
    main()
