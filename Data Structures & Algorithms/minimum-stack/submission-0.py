class MinStack:

    def __init__(self):
        self.s = []
        

    def push(self, val: int) -> None:
        self.s.append(val)

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        if self.s:
            result = self.s[0]
        for i in self.s:
            print(i)
            if result > i:
                result = i
        return result

