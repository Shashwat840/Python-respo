class Demo:
    count = 0
    def fun(self, *args):
        for i in args:
            if str(i) is True:
                self.count+=1
        if i == self.count:
            return sum(args)
        else:
            print("All values are not number")

d = Demo()
d.fun(10,20,30)
print(d.count)  