
class Fastpass(object):

    def __init__(self, name):
        self.__name = name
        self.__available = True
        self.__lower = 0
        self.__upper = 0


    def setTime(self, lower):
        self.__lower = lower
        self.__upper = lower + 60


    def isInTime(self, time):
        if(time > self.__lower and time < self.__upper):
            return True
        else:
            return False


    def enable(self):
        self.__available = True


    def disable(self):
        self.__available = False


    def isAvailable(self):
        return self.__available


    def getName(self):
        return self.__name
