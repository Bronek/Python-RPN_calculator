class RPN():
    stack = []
    def __init__(self, *args):
        for arg in args:
            if isinstance(arg, int) or isinstance(arg, float):
                self.stack.append(float(arg))
        print(self.stack)

    def stackadd(self, *args):
        for arg in args:
            if isinstance(arg, int) or isinstance(arg, float):
                self.stack.append(float(arg))
        print(self.stack)

    def add(self):
        if len(self.stack) >= 2:
            a = self.stack[-1] + self.stack[-2]
            for i in range(2):
                self.stack.pop(-1)
            self.stack.append(a)
        print(self.stack)

    def subtract(self):
        if len(self.stack) >= 2:
            a = self.stack[-1] - self.stack[-2]
            for i in range(2):
                self.stack.pop(-1)
            self.stack.append(a)
        print(self.stack)

    def multiply(self):
        if len(self.stack) >= 2:
            a = self.stack[-1] * self.stack[-2]
            for i in range(2):
                self.stack.pop(-1)
            self.stack.append(a)
        print(self.stack)

    def divide(self):
        if len(self.stack) >= 2:
            a = self.stack[-1] / self.stack[-2]
            for i in range(2):
                self.stack.pop(-1)
            self.stack.append(a)
        print(self.stack)

    def power(self):
        if len(self.stack) >= 2:
            a = self.stack[-2] ** self.stack[-1]
            for i in range(2):
                self.stack.pop(-1)
            self.stack.append(a)
        print(self.stack)
