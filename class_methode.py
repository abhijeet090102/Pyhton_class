class rectangle:
    def __init__(self,wi,he):
        self.width = wi
        self.height = he
    def cal(self):
        return self.width*self.height
    @classmethod
    def new_sq(cls,side_len):
        return cls(side_len,side_len)
sq = rectangle.new_sq(6)
print(sq.cal())
