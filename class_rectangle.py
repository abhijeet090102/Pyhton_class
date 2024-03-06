'''class rectangle:
    def setdata(self):
        self.length = int(input('Enter any length value'))
        self.breadth = int(input('Enter any breadth value'))
    def putdata(self):
        print('The lenght is ',self.length)
        print('The breadth is ',self.breadth)
    def area(self):
        a = self.length*self.breadth
        return print('Area is =',a)
    def perimeter(self):
        p = 2*(self.length+self.breadth)
        return print('Perimeter is = ',p)
    def setlength(self):
        ca = input("Do you want to change lenght choose y/n ")
        if ca == 'y':
            self.length = int(input("Enter new length value"))
r = rectangle()
r.setdata()
r.putdata()
r.area()
r.perimeter()
r.setlength()
r.putdata()

'''
'''# constructor
class rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b 
    def putdata(self):
        print('The length is ',self.length)
        print('The breadth is ',self.breadth)
    def setlenbread(self):
        self.length = int(input('Enter new length'))
        self.breadth = int(input('Enter new breadth'))
    def area(self):
        self.area = self.length * self.breadth
        print('The area of rectangle is :',self.area)
r1 = rectangle(10,20)
r1.putdata()
r2 = rectangle(40,50)
r2.putdata()
r1.setlenbread()
r2.setlenbread()
r1.area()
r2.area()
'''
'''# destructur
class rectangle:
    count = 0
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        rectangle.count +=1
    def __del__(self):
        print(f'one object is deleted')
        rectangle.count -= 1
    def display(self):
        print(self.length)
        print(self.breadth)
    def __str__(self):
        return 'length :' + str(self.length)+ ' '+ 'breadth:' + str(self.breadth)
r1 = rectangle(10,20)
r2 = rectangle(40,6)
r1.display()
print(rectangle.count)
del r1
print(rectangle.count)
print(r2)
#print(r1)'''
'''
class rectangle:
    count = 0
    def __init__(self,l,b):
        self.__length = l
        self.breadth = b
        rectangle.count +=1
    def __del__(self):
        print(f'one object is deleted')
        rectangle.count -= 1
    def area(self):
        self.area = self.__length * self.breadth
        print(self.area)
    def __str__(self):
        return 'length :' + str(self.length)+ ' '+ 'breadth:' + str(self.breadth)
r1 = rectangle(12,6)
print(r1.breadth)
r1.area()
print(__length)
'''

