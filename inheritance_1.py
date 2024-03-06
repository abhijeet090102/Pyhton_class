class person:
    def __init__(self,n,p):
        self.__name = n
        self.phone = p
    def show(self):
        print('Person Name '+ self.__name+ '\nPhone no ',self.phone)
class student(person):
    def __init__(self,n,p,ro,co):
        person.__init__(self,n,p)
        self.roll = ro
        self.course = co
    def display(self):
        person.show(self)
        print('Roll no: ',self.roll)
        print('Course name :',self.course)
p1 = person('abhijeet',6203269737)
p1.show()

st = student('abhijeet',6203269737,1,'MCA')
st.display()
