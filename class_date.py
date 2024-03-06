class Mydata:
    def setdate(self):
        self.day = int(input('Enter  the day date between 1 to 30 :'))
        self.month = int(input('Enter the month of date between 1 to 12 :'))
        self.year = int(input('Enter the yera of date'))

    def checkdate(self):
        print('The valid date is : {self.day}/{self.month}/{self.year}')
    def adddays(self):
        dday = int(input('How many days you want to add '))
        self.day += dday
        if self.day>60 and self.day<60:
            
