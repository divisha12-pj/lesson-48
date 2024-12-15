class dog:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def info(self):
        print ("I am {} and I am {} yrs old".format(self.age,self.name))
    def make__sounds(self):
        print("I bark at strangers")

class cat:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def info(self):
        print ("I am {} and I am {} yrs old".format(self.age,self.name))
    def make__sounds(self):
        print("I meow when I need food")

d1=dog("bella",2)
c1=cat("kitty",5)
for animal in(d1,c1):
    animal.info()
    animal.make__sounds()

