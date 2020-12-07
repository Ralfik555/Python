class NETFLIXException(Exception):
    def __init__(self,text,area):
        super().__init__(text)
        self.area = area

    def __str__(self):
        return "{}, area {}".format(super(NETFLIXException, self).__str__(),self.area)


class NETFIXSecurityException(NETFLIXException):
    pass

class NETFIXDataFormatException(NETFLIXException):
    pass


try:
    # do somethign...
    raise NETFLIXException("file format is incorrect","Personal Information")
except NETFIXSecurityException as e:
    print("Application security error {}".format(e))
except NETFIXDataFormatException as e:
    print("Application data format error {}".format(e))
except NETFLIXException as e:
    print("Application error {}".format(e))
except Exception as e:
    print("General error {}".format(e))