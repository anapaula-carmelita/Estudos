class WeekDayError(Exception):
    pass

class Weeker:
    __valid_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        # Valida se o dia passado está na nossa lista de dias válidos
        if day not in Weeker.__valid_days:
            raise WeekDayError
        
        # Guarda o dia atual
        self.__current_day = day

    def __str__(self):
        return self.__current_day

    def add_days(self, n):
        indexday = Weeker.__valid_days.index(self.__current_day)

        indexday = (indexday + n) % 7
        
        self.__current_day = Weeker.__valid_days[indexday]


    def subtract_days(self, n):
        indexday = Weeker.__valid_days.index(self.__current_day)

        indexday = (indexday - n) % 7
        
        self.__current_day = Weeker.__valid_days[indexday]
        

