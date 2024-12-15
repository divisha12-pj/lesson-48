class computer:
    def __init__(self):
        self.__maxprice=9000

    def sell(self):
        print("selling price is",self.__maxprice)

    def setmaxprice(self,price):
        self.__maxprice=price


c1=computer()
c1.sell()

c1.__maxprice=10000
c1.sell()

c1.setmaxprice(10000)
c1.sell()
        