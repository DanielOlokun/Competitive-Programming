# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# O(1) time complexity !!!!!


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:    # if min stack is empty etc etc...
            self.min_stack.append(val)
        
    def pop(self):
        val = self.stack.pop()

        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val
        
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]

  # the logic behing this is I used two stacks - one stack to keep track of all numbers and another to keep track of minimums at every point
  # hence why two stacks (stack and min_stack) are initially initialised 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
