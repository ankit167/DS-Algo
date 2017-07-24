class Circular_Queue:

    def __init__(self, size):
        self.a = [None for i in range(size)]
        self.front = -1  # Pointer to start of the queue
        self.rear = -1  # Pointer to end of the queue
        self.size = size  # Size of the queue

    # Move to next index. If empty, fill the index.
    def push(self, data):
        if self.size == 0:
            print 'Queue size should be more than 0'
            return
        print 'Pushing %s' % data

        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
            self.a[self.rear] = data
            return

        index = (self.rear + 1) % self.size
        if index == self.front:
            print "Can't push. Queue is full."
            return
        self.rear = index
        self.a[self.rear] = data

    # Delete current index, and move to next index.
    def pop(self):
        if self.size == 0:
            print 'Queue size should be more than 0'
            return
        if self.front == -1 or self.a[self.front] == -1:
            print "Can't pop. Queue is empty."
            return
        print 'Popped %s' % self.a[self.front]

        self.a[self.front] = -1
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    # Print the current state of the queue
    def print_queue(self):
        print 'Front- %s Rear- %s' % (self.front, self.rear)
        if self.front == -1 and self.rear == -1:
            print 'Queue is empty'
            print
            return

        c = self.front
        while c != self.rear:
            print self.a[c],
            c = (c + 1) % self.size
        print self.a[c]
        print


def main():
    cq = Circular_Queue(5)
    cq.push(1)
    cq.print_queue()

    cq.pop()
    cq.print_queue()

    cq.pop()
    cq.print_queue()

    cq.push(2)
    cq.print_queue()

    cq.push(3)
    cq.print_queue()

    cq.pop()
    cq.print_queue()

    cq.push(4)
    cq.print_queue()

    cq.push(5)
    cq.print_queue()

    cq.push(6)
    cq.print_queue()

    cq.pop()
    cq.print_queue()

    cq.push(7)
    cq.print_queue()

    cq.push(8)
    cq.print_queue()

    cq.push(9)
    cq.print_queue()

    cq.pop()
    cq.print_queue()

    cq.pop()
    cq.print_queue()

if __name__ == '__main__':
    main()
