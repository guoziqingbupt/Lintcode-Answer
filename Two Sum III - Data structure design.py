class TwoSum:
    """
    @param: number: An integer
    @return: nothing
    """

    def __init__(self):
        self.record = {}

    def add(self, number):
        if number not in self.record:
            self.record[number] = 1
        else:
            self.record[number] += 1
        # write your code here

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        for ele in self.record:
            gap = value - ele
            self.record[ele] -= 1
            if gap in self.record and self.record[gap] != 0:
                self.record[ele] += 1
                return True
            self.record[ele] += 1
        return False
        # write your code here

obj = TwoSum()
obj.add(2)
obj.add(3)
obj.find(4)
obj.find(5)
print(obj.find(6))