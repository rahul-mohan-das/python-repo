class dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fn(self,a):
        print(a,self.name,self.age)
dog1=dog("Terry",2)
dog1.fn("hi")
         
