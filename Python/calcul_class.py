class FourCal():
	def setdata(self,a,b):
		self.a=a
		self.b=b
	def add(self):
		return self.a+self.b
	def sub(self):
		return self.a-self.b
	def mul(self):
		return self.a*self.b
	def div(self):
		return self.a/self.b

class cal2(FourCal):
    def pow(self):
        return self.a**self.b
    def div(self):
        if self.b==0:
            return 0
        else:
            return super().div()
            
second = cal2()
second.setdata(9,0)
print(second.pow())
print(second.div())
