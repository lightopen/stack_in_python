class Stack(object):
    """
       stack by python
       filo先入后出
       默认容量为4
    """
    def __init__(self, capacity=4):
        self.clear()
        self.capacity = capacity
        

    # 计数
    def count(self):
        return self.height

    # 判满
    def full(self):
        if self.height == self.capacity:
            return True
        return False

    # 判空
    def empty(self):
        if self.height == 0:
            return True
        return False

    # 清空栈
    def clear(self):
        self.top = 0
        self.height = 0
        self.__stack = []

    # 插入栈 -filo
    def push(self, value):
        if self.full():
            return False
        self.__stack.append(value)
        self.height += 1
        self.top += 1

    # 出栈 -filo
    def pop(self):
        if self.empty():
            return False
        value = self.__stack.pop()
        self.height -= 1
        self.top -= 1
        return value

    # 实现迭代
    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == self.height:
            raise StopIteration
        return self.__stack[self.index]
        
