'''class Person:
    count = 0
    def __init__(self,name,DOB,address):
        self.name = name
        self.DOB = DOB
        self.address = address
        Person.count += 1
    def getName(self):
        return self.name
    def getDOB (self):
        return self.DOB
    def getAddress(self):
        return self.address
    def setName(self,name):
        self.name = name
    def setDOB (self,DOB):
        self.DOB = DOB
    def setAddress(self,address):
        self.address = address
    def getCount(self):
        return Person.count
    def __str__(self):
        return 'Name:'+self.name+'\nDOB:'+str(self.DOB)\
               +'\nAddress:'+self.address
p1 = Person('Abhijeet','09-01-2002','40/6 malda')
#p1.__str__()
    #'Name:Abhijeet\nDob:09-01-2002\nAddress:40/6,Malda '
print(p1.__str__())
'''
class Bird:
    count =0
    def __init__(bird,name,Sound):
        bird.name = name
        bird.Sound = Sound
        bird.count += 1
    def getName(bird):    
        return bird.name
    def getSound(bird):
        input("Enter bird Sound")
        return bird.Sound
    def setName(bird):
        bird.name = name
    def setSound(bird):
        bird.Sound = Sound
    def __str__(bird):
        return 'Name:'+bird.name+ '\nSound:' +bird.Sound
bi = Bird(input("Enter name ") , input("Enter Sound"))
b1= Bird('Eagle' , 'Scream')
print(bi.__str__())
print(b1.__str__())

