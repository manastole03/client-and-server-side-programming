def is_date_valid(d, m, y): 
    if type(d) != int:
        raise TypeError("Bad type:day")
    if type(m) != int:
        raise TypeError("Bad type:Month")
    if type(y) != int:
        raise TypeError("Bad type:Year")
    def is_leap_year(y):
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True 
        else:
            return False
    
    is_leap = is_leap_year(y)

    if not m in range(1, 13):
        return False

    if m == 2 and is_leap == True:
        if d in range(1, 30):
            return True
        else:
            return False
    elif m == 2 and is_leap == False:
        if d in range(1, 29):
            return True
        else:
            return False
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        if d in range(1, 32):
            return True
        else:
            return False
    elif m in [4, 6, 9, 11]:
        if d in range(1, 31):
            return True
        else:
            return False
        
class Date:
    def __init__(self, init_d, init_m, init_y):
        if not is_date_valid(init_d, init_m, init_y):
            raise ValueError("Bad date value")
        self.day = init_d
        self.month = init_m
        self.year = init_y

    def get_day(self):
        print("type(self):", type(self))
        print("id(self):", id(self))

        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def set_day(self, new_d):
        if is_date_valid(new_d, self.month,
                            self.year):
            self.day = new_d

    def set_month(self, new_m):
        if is_date_valid(self.day, new_m,
                         self.year):
            self.month = new_m

    def set_year(self, new_y):
        if is_date_valid(self.day, self.month,
                        new_y):
            self.year = new_y
    
        
# Client

def main():
    d1 = Date(20, 4, 1990)
    d2 = Date(20, 3, 1999)

    print("main:id(d1):", id(d1))
    dd = d1.get_day()
    print("main:dd:", dd)
    print("-" * 50)

    mm = d1.get_month()
    print("mm:", mm)
    yy = d1.get_year()
    print("yy:", yy)

    d1.set_day(17)
    d1.set_month(3)
    d1.set_year(2045)

    print(d1.get_day(), d1.get_month(), d1.get_year())
    
main() 

