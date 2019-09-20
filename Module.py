import time
class Date(object):
    def __init__(self, year , month, day):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls,s):
        parts = s.split('-')
        return cls(int(parts[0]),int(parts[1]),int(parts[2]))


    @classmethod
    def todaydate(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def birthyr(self):
      print("hello person")


class Person(Date):
    def x(name):
        print("this is just a function")