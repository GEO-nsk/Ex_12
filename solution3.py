class Meeting:
    '''
    Description of class of meetings

    class attributes:
    lst_meeting: list with all meetings

    Attributes:
        id: number of meeting
        date: date of meeting
        title: name of meeting
        employees: list with list of employee's ids

    methods:
        add_person: adds new person to lst_user and adds id to employees
        count: counts number of employees at meeting
        count_meeting: returnes number of meetings in selected date
        total: returnes all employees from all meetings
    '''
    lst_meeting = []

    def __init__(self, id=None, date=None, title=None, employees=None):
        self.id = id
        self.date = date
        self.title = title
        self.employees = employees

    def add_person(self, person):
        '''
        adds new person to lst_user and adds id to employees
        person: string with info about new person
        '''
        user = User(person.split(';')[0], person.split(';')[1], person.split(';')[2], person.split(';')[3],
                    person.split(';')[4], person.split(';')[5], )
        User.lst_user.append(user)
        self.employees.append(person.split(';')[0])

    def count(self):
        '''
        counts number of employees at meeting
        '''
        print(len(self.employees))

    @classmethod
    def count_meeting(cls, date):
        '''
        returnes number of meetings in selected date
        date: selected date
        returns number of meetings
        '''
        cnt = 0
        for item in cls.lst_meeting:
            date1 = Date(item.date)
            if date1.to_timestamp() == date.to_timestamp():
                cnt += 1
        return cnt

    @classmethod
    def total(cls):
        '''
        returnes all employees from all meetings
        '''
        cnt = 0
        for item in cls.lst_meeting:
            cnt += len(item.employees)
        return cnt

    def __repr__(self):
        out_list = []
        for itr in self.employees:
            for item in User.lst_user:
                if int(itr) == int(item.id):
                    out_line = f'ID: {item.id} LOGIN: {item.nick_name} NAME: '
                    if item.first_name != '':
                        out_line += f'{item.first_name} '
                    if item.last_name != '':
                        out_line += f'{item.last_name} '
                    if item.middle_name != '':
                        out_line += f'{item.middle_name} '
                    if item.gender != '':
                        out_line += f'GENDER: {item.gender}'
                    out_list.append(out_line)

        out_list_str = '\n'.join(out_list)
        return f'Рабочая встреча {self.id}\n{self.date} {self.title}\n{out_list_str}\n'


class User:
    lst_user = []

    def __init__(self, id=None, nick_name=None, first_name=None, last_name=None, middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __repr__(self):
        return f'{self.id} {self.nick_name} {self.first_name} {self.last_name} {self.middle_name} {self.gender}'


class Load:
    '''
    This class can load info from files

    methods:
        write: function load info from file
    '''
    @classmethod
    def write(cls, file_name_meetings, file_name_persons, file_name_pers_meeitngs):
        '''
        function load info from file
        '''
        with open(file_name_persons, 'r', encoding='utf-8') as ptr:
            next(ptr)
            for line in ptr:
                user = User(line.split(';')[0], line.split(';')[1], line.split(';')[2], line.split(';')[3],
                            line.split(';')[4], line.split(';')[5], )
                User.lst_user.append(user)

        with open(file_name_meetings, 'r', encoding='utf-8') as ptr:
            next(ptr)
            for line in ptr:
                pers_list = []
                with open(file_name_pers_meeitngs, 'r', encoding='utf-8') as ptr_pers:
                    next(ptr_pers)
                    for itr in ptr_pers:
                        if line.split(';')[0] == itr.split(';')[0]:
                            pers_list.append(itr.split(';')[1])
                meeting = Meeting(line.split(';')[0], line.split(';')[1], line.split(';')[2], pers_list)
                Meeting.lst_meeting.append(meeting)

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
        to_timestamp: function converts date to seconds from 01.01.1970
    '''

    all_month = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн', 7: 'июл',
                 8: 'авг', 9: 'сен', 10: 'окт', 11: 'ноя', 12: 'дек', }

    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]

    def __init__(self, str_date):
        self._date = str_date

    def to_timestamp(self):
        '''
        function converts date to seconds from 01.01.1970

        returnes number with seconds from 01.01.1970
        '''
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