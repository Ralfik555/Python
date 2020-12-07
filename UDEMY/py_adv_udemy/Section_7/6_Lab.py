import datetime as dt

class TripException(Exception):
    def __init__(self,text,description):
        super(TripException, self).__init__(text)
        self.description = description

    def __str__(self):
        return "{}, description: {}".format(super(TripException, self).__str__(),self.description)


class TripNameException(TripException):
    def __init__(self,text):
        super(TripNameException, self).__init__(text,'Name of the trip is missing. You need to name the trip somehow...')

class TripDateException(TripException):
    def __init__(self,text):
        super(TripDateException, self).__init__(text,'The dates are incorrect. The starting date should be earlier than the ending date...')


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException("Title error!")
        if self.start > self.end:
            raise TripDateException("Date error!")

    @classmethod
    def publish_offer(cls,list_of_trips):
        list_of_errors = []
        for trip in list_of_trips:
            try:
                trip.check_data()
            except TripNameException as e:
                list_of_errors.append("<{}>:<{}>".format(trip.symbol,e))
            except TripDateException as e:
                list_of_errors.append("<{}>:<{}>".format(trip.symbol,e))

        if len(list_of_errors) > 0:
            raise TripException("The list of trips has errors", list_of_errors)
        else:
            print('the offer will be published...')


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]


try:
    print("Checking trips offer...")
    Trip.publish_offer(trips)
    print("DONE")
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')


