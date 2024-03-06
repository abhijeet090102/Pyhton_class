class item :
    def __init__(self, n , pr,q):
        self.name = n
        self.price = pr
        self.quantity = q
    def purchase(self):
        print(f'Name of an item {self.name}')
        self.no = int(input(f'Enter the no of item you want to purchase'))
        self.quantity = self.quantity - self.no
    def increasestock (self):
        print(f'Name of an item {self.name}')
        self.num = int(input('Enter new item quantity'))
        self.quantity = self.quantity+self.num
    def display(self):
        print(f'Name of an item is {self.name} , Price of an item {self.price} , Quantity of an item {self.quantity}')
i1 = item ('laptop',60000,40)
i2 = item ('tv',100000,46)
i1.purchase()
i1.display()
i2.purchase()
i2.display()
i1.increasestock()
i2.increasestock()
i1.display()
i2.display()
