class MinStack:
    def __init__(self):
        self.stack = []

    # do intialization if necessary

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        self.stack.append(number)

    # write your code here

    """
    @return: An integer
    """

    def pop(self):
        return self.stack.pop()

    # write your code here

    """
    @return: An integer
    """

    def min(self):
        return min(self.stack)

# write your code here
