class AirTicket:
    '''
    Description of class of tickets

    This class can show ait ticket

    Attributes:
        passenger_name: name of passanger
        _from: arrival airport
        to: destination airport
        date_time: date and time of flight
        flight: number of flight
        seat: number of seat
        _class: passenger's class
        gate: passenger's gate
    '''
    def __init__(self, passenger_name, _from, to, date_time, flight, seat, _class, gate):
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __str__(self):
        return (f'|{self.passenger_name}{" " * (16 - len(self.passenger_name))}|'
                f'{self._from} |{self.to}|{self.date_time}|{self.flight}{" " * (20 - len(self.flight))}|'
                f'{self.seat}{" " * (4 - len(self.seat))}|{self._class}  |{self.gate}  |')

class Load:
    '''
    This class can load info from files

    class attributes:
        data: list with all information from file

    methods:
        write: function load info from file
    '''
    data = []
    @classmethod
    def write(cls, file_name):
        '''
        function load info from file
        '''
        with open(file_name, 'r', encoding='utf-8') as ptr:
            next(ptr)
            for line in ptr:
                passenger = AirTicket(line.split(';')[0], line.split(';')[1], line.split(';')[2], line.split(';')[3],
                                      line.split(';')[4], line.split(';')[5], line.split(';')[6], line.split(';')[7][0:2])
                cls.data.append(passenger)