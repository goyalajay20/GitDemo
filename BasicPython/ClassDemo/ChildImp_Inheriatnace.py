from classDe import Calculator

class childimpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2,3)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj1 = childimpl()
print(obj1.getCompleteData())