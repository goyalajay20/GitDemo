class Calculator:
    num = 100 # class variable

    def __init__(self,a,b):
        self.firstNumer = a
        self.secondNumber = b
        print("I am automatically called when object is created")
    def getData(self, num=num):
        print("I am now executing as method in class")
        print(num)
        #print(num)

    def Summation(self):
        return self.firstNumer+self.secondNumber+self.num
        #return self.firstNumer + self.secondNumber + Calculator.num

obj = Calculator(3,2)
obj.getData()
print(obj.Summation())


