# polymorphism
class rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    def __add__(self,r):
        nr = rectangle(0,0)
        nr.length = self.length + r.length
        nr.breadth = self.breadth
        return nr
    
    def __self__(self):
        return 'Old Length '+ str(self.length)+ ' '+ 'Breadth '+ str(self.breadth)+ 'New length '+ str(nr.length) + ' '+ 'new breadth '+ str(nr.breadth)
r1 = rectangle(4,6)
print(r1)
r2 = rectangle(2,8)
#r1.display()
