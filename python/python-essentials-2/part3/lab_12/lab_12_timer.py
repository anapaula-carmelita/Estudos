class Timer:
    def __init__(self, hour=0, min=0, sec=0):
        self.__hour = hour
        self.__min = min
        self.__sec = sec

    def __str__(self):
        hour, min, sec = '', '', ''
        if self.__hour < 10:
            hour = '0' + str(self.__hour)
        else: hour = str(self.__hour)
        if self.__min < 10:
            min = '0' + str(self.__min)
        else: min = str(self.__min)
        if self.__sec < 10:
            sec = '0' + str(self.__sec)
        else: sec = str(self.__sec)
        
        
        return hour + ':' + min + ':' + sec 
    
    def next_second(self):
        if self.__sec == 59:
            self.__sec = 0
            
            if self.__min == 59: 
                self.__min = 0
                
                if self.__hour == 23:
                    self.__hour = 00
                else: self.__hour += 1

            else: self.__min += 1

        else:
            self.__sec += 1

    def prev_second(self):
        if self.__sec == 00:
            self.__sec = 59
            
            if self.__min == 00: 
                self.__min = 59
                
                if self.__hour == 00:
                    self.__hour = 23
                else: self.__hour -= 1

            else: self.__min -= 1

        else:
            self.__sec -= 1
