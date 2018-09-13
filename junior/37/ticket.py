class Ticket:
    workday_price = 100
    weekend_rate = 1.2
    child_rate = 0.5
    is_weekend = False

    def get_adult_price(self):
        return self.workday_price if (self.is_weekend is False) else (self.workday_price * self.weekend_rate)

    def get_child_price(self):
        adult_price = self.get_adult_price()
        print(adult_price, self.child_rate)
        
        return adult_price * self.child_rate

    def set_child_rate(self, rate):
        self.child_rate = rate

    def set_weekend(self, is_weekend):
        self.is_weekend = is_weekend


t = Ticket()

t.is_weekend = False

a_price = t.get_adult_price()
c_price = t.get_child_price()

total_price = a_price * 2 + c_price

print(total_price)
    
