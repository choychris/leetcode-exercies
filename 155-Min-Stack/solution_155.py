"""

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = []
        self.minIndex = []

    def push(self, val: int) -> None:

        if len(self.minIndex) == 0:
            self.minIndex = [0]
        elif val <= self.head[self.minIndex[-1]]:
            self.minIndex.append(len(self.head))

        self.head.append(val)

    def pop(self) -> None:
        self.head.pop()
        if len(self.head) == self.minIndex[-1]:
            self.minIndex.pop()

    def top(self) -> int:
        return self.head[-1]

    def getMin(self) -> int:
        return self.head[self.minIndex[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
