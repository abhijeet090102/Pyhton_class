class person:
    count = 0
    def __init__(self,n,d,ad):
        self.name = n
        self.DOB = d
        self.address = ad
        person.count += 1
    def getname (self):
        print(f'Your name is {self.name}')
    def dob(self):
        print(f'Your DOB is {self.DOB}')
    def getaddress(self):
        print(f'Your address is {self.address}')
    def setname(self):
        self.name = input('Enter your name ')
    def setdob(self):
        self.DOB = (input('Enter your dob '))
    def setadd(self):
        self.address= input('Enter your new address ')
    def __str__(self):
        #return f'Your name is {self.name}  DOB is {self.DOB} Address is {self.address} '
        return 'Your name is ',self.name  ,'DOB is ',self.DOB ,'Address is ',self.address
p1 = person('abhi','9/11/2002','pakur jh')
p1.getname()
p1.dob()
p1.getaddress()
p1.setname()
p1.setdob()
p1.setadd()
print(p1.__str__())
#person.count()
