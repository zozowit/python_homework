class Stack:
    def __init__(self):
        self.stack_list = []

    def isEmpty(self):
        if (len(self.stack_list) == 0):
            return True
        else:
            return False

    def push(self, item):
        self.stack_list.insert(0, item)

    def pop(self):
        if self.isEmpty():
            return False
        else:
            return self.stack_list.pop()

    def top(self):
        if self.isEmpty():
            return False
        else:
            return self.stack_list[0]

    def bottom(self):
        stack_len = len(self.stack_list)

        if stack_len > 0:
            return self.stack_list[stack_len-1]
        else:
            return false
