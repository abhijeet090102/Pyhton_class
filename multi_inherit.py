#class inheritance - Multiple inheritance using constructur
class student:
    def __init__(self,n,r):
        self.name = n
        self.roll = r
    def __str__(self):
        return 'Name :' +self.name+ ' Roll no: ' + self.roll
class makautstudent(student):
    def __init__(self,n,r,reg):
        student.__init__(self,n,r)
        self.reg_no = reg
    def show(self):
        return self.name , self.roll, self.reg_no
st1= student('Abhijeet',1)
st1.makautstudent(65642634)
st1.show()
        
