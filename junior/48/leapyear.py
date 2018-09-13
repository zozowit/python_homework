class LeapYear():
    def __init__(self, year = 2018):
        self.leap_year = []
        self.until = year
        for each in range(self.until):
            if (each%4 == 0 and each%100 != 0) or (each % 400 == 0):
                self.leap_year.append(each)
                
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.leap_year.pop()
        except IndexError:
            raise StopIteration
