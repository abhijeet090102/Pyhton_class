'''class rectangle:
    def __init__ (self,l,b):
        self.__length = l
        self.breadth= b
    def area(self):
        self.area = self.__length * self.breadth
        return self.area
r1 = rectangle(10,3)
print(r1.breadth)
# print(r1.__length) -- it shows error
print(r1.area())
'''

class student:
    def __init__(self,n,r,ma):
        self.name =n
        self.roll = r
        self.__marks = ma
    def __str__ (self):
        return 'Name:'+self.name +' '+'Roll no '+str(self.roll)+' '+'Marks'+str(self.__marks)
    def setmarks(self):
        self.__marks = int(input('Enter marks'))
r1 = student('Abhijeet',1,90)
print(r1)
r1.setmarks()
print(r1)

