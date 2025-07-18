class WeekDayError(Exception):
    pass

class Weeker:
    __names = ["Mon", "Tue","Wed", "Thu", "Fri", "Sat", "Sun"]
    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError
            
    def __str__(self):
        return Weeker.__names[self.__current]
        
    def add_day(self, n):
        self.__current = (self.__current + n) % 7
        
    def subtract_day(self, n):
        self.__current = (self.__current - n) % 7
           
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_day(15)
    print(weekday)
    weekday.subtract_day(23)
    print(weekday)
    weekday = Weeker("Monday")
except WeekDayError:
    print("Sorry, I can't server your request")


'''
Output:
Mon
Tue
Sun
Sorry, I can't server your request
'''
