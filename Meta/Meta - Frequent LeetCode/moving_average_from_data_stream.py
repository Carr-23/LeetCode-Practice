class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.movAvg = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.movAvg.append(val)
        if len(self.movAvg) > self.size:
            del self.movAvg[0]

        return sum(self.movAvg) / float(len(self.movAvg))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
