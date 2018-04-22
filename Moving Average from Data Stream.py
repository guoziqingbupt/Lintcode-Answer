class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.sum = 0
        self.count = 0
        self.record = []
        # do intialization if necessary

    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        if self.count < self.size:
            self.record.append(val)
            self.count += 1
            self.sum += val
            return self.sum / self.count
        else:
            self.sum -= self.record[0]
            self.sum += val
            self.record.pop(0)
            self.record.append(val)

        return self.sum / self.count
        # write your code here


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)