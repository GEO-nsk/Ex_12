class Date:
    '''
    Description of class of date

    This class helps to convert date

    Class attributes:
        all_mounth: dictionary with number of month and first 3 russian symbols of each month
        days_31: list with numbers of month with 31 days
        days_30: list with numbers of month with 30 days

    Attributes:
        _date: string with date

    Methods:
            is_date: function returns None if date isn't correct
            date_to_str: function converts date to string
            to_timestamp: function converts date to seconds from 01.01.1970
    '''

    all_month = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн', 7: 'июл',
                 8: 'авг', 9: 'сен', 10: 'окт', 11: 'ноя', 12: 'дек', }

    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]

    def __init__(self, str_date):
        if self.is_date(str_date) == True:
            self._date = str_date
        else:
            print('ошибка')
            self._date = None

    @property
    def date(self):
        if self.is_date(self._date):
            return self.date_to_str()
        else:
            return None

    @date.setter
    def date(self, value):
        if self.is_date(value):
            self._date = value
        else:
            print('ошибка')
            self._date = None

    @date.getter
    def date(self):
        if self.is_date(self._date):
            return self.date_to_str()
        else:
            return None
    def is_date(self, str_date):
        '''
        function returns None if date isn't correct

        returns: True of False if date is correct
        '''
        if str_date != None:
            flag = True
            if len(str_date) <= 10 and len(str_date) >= 7:
                day = int(str_date.split('.')[0])
                month = int(str_date.split('.')[1])
                year = int(str_date.split('.')[2])
                if month in self.days_31:
                    if day > 31 or day < 1:
                        flag = False
                if month in self.days_30:
                    if day > 30 or day < 1:
                        flag = False
                if month == 2:
                    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                        if day > 29 or day < 1:
                            flag = False
                    else:
                        if day > 28 or day < 1:
                            flag = False

                if month > 12 or month < 1:
                    flag = False
                if year < 1:
                    flag = False

            else:
                flag = False
        else:
            flag = False

        return flag

    def date_to_str(self):
        '''
        function converts date to string

        returns string with date
        '''
        if self._date != None:
            day = int(self._date.split('.')[0])
            month = int(self._date.split('.')[1])
            year = int(self._date.split('.')[2])
            result = ''
            result += str(day)
            result += ' '
            for k, v in self.all_month.items():
                if k == month:
                    result += v
            result += ' '
            result += str(year)
            return result
        else:
            return None

    def to_timestamp(self):
        '''
        function converts date to seconds from 01.01.1970

        returnes number with seconds from 01.01.1970
        '''
        if self._date != None:
            day = int(self._date.split('.')[0])
            month = int(self._date.split('.')[1])
            year = int(self._date.split('.')[2])
            res = 0
            for itr in range(1970, year):
                if (itr % 4 == 0 and itr % 100 != 0) or (itr % 400 == 0):
                    res += 366 * 24 * 60 * 60
                else:
                    res += 365 * 24 * 60 * 60

            for itr in range(1, month):
                if itr in self.days_31:
                    res += 31 * 24 * 60 * 60
                elif itr in self.days_30:
                    res += 30 * 24 * 60 * 60
                elif itr == 2:
                    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                        res += 29 * 24 * 60 * 60
                    else:
                        res += 28 * 24 * 60 * 60

            for itr in range(1, day):
                res += 24 * 60 * 60

            return res
        else:
            return None

    def __eq__(self, other):
         return self.to_timestamp() == other.to_timestamp()

    def __ne__(self, other):
        return self.to_timestamp() != other.to_timestamp()

    def __lt__(self, other):
        return self.to_timestamp() < other.to_timestamp()

    def __gt__(self, other):
        return self.to_timestamp() > other.to_timestamp()

    def __le__(self, other):
        return self.to_timestamp() <= other.to_timestamp()


    def __ge__(self, other):
        return self.to_timestamp() >= other.to_timestamp()

    def __repr__(self):
        self.is_date(self._date)
        return f'{self.date_to_str()}'

    def __str__(self):
        self.is_date(self._date)
        return f'{self.date_to_str()}'