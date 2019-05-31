class RPN():
    stack = []
    def __init__(self, *args):
        for arg in args:
            try:
                self.stack.append(int(arg))
            except:
                pass
        print(self.stack)

    def stackadd(self, *args):
        for arg in args:
            try:
                self.stack.append(int(arg))
            except:
                pass
        print(self.stack)

    def add(self):
        try:
            a = self.stack[-1] + self.stack[-2]
            self.stack.pop(-1)
            self.stack.pop(-1)#original [-2] is [-1] after previous pop()
            self.stack.append(a)
        except:
            pass
        print(self.stack)

    def subtract(self):
        try:
            a = self.stack[-1] - self.stack[-2]
            self.stack.pop(-1)
            self.stack.pop(-1)#original [-2] is [-1] after previous pop()
            self.stack.append(a)
        except:
            pass
        print(self.stack)

    def multiply(self):
        try:
            a = self.stack[-1] * self.stack[-2]
            self.stack.pop(-1)
            self.stack.pop(-1)#original [-2] is [-1] after previous pop()
            self.stack.append(a)
        except:
            pass
        print(self.stack)

    def divide(self):
        try:
            a = self.stack[-1] / self.stack[-2]
            self.stack.pop(-1)
            self.stack.pop(-1)#original [-2] is [-1] after previous pop()
            self.stack.append(a)
        except:
            pass
        print(self.stack)

    def power(self):
        try:
            a = self.stack[-2] ** self.stack[-1]
            self.stack.pop(-1)
            self.stack.pop(-1)#original [-2] is [-1] after previous pop()
            self.stack.append(a)
        except:
            pass
        print(self.stack)