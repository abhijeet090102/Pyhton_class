'''class student:
    def setdata(self):
        self.rollno = int(input("Enter your roll no "))
        self.course = input('Enter your course ')
        self.name = input('Enter your name ')
    def putdata(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
s1 = student() #callling a object
s1.setdata() # puuting values 
s2 = student()
s2.setdata()
s1.putdata()
s2.putdata()
'''
'''
#constructur
class student:
    def __init__(self,n,r):
        self.name = n
        self.roll = r
    def display(self):
        print('Name is: ',self.name)
        print('Roll no is: ',self.roll)
st1= student('Abhijeet',1)
st1.display()
st2= student('Manisha',1)
st2.display()
'''
'''
# class member
class student:
    count = 0
    def __init__(self,n,r):
        self.name = n
        self.roll = r
        student.count += 1
    def display(self):
        print('Name is : ',self.name)
        print('Roll_no is : ',self.roll)
st1= student('Abhijeet',1)
st1.display()
st2= student('Manisha',1)
st2.display()
print('Total no of student is : ',student.count)
'''
#Destructor
class student:
    count = 0
    def __init__(self,n,r):
        self.name = n
        self.roll = r
        student.count +=1
    def __del__(self):
        print('One object is deleted ')
        student.count -= 1
    def display(self):
        print(self.name)
        print(self.roll)
def main():
    st1 = student('Abhijeet',1)
    st2 = student('Manisha',1)
    st3 = student('ma',6)
    st1.display()
    st2.display()
    del st3
    print(st1.name)
    print(st2.name)
main()
    
