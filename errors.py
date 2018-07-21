#TODO fix this later

class Error(Exception):
    def __init__(self, error_type=None, mesg=None):
        self.error_type = error_type
        self.mesg = mesg
        self.trace = None

    def __str__(self):
        return "%s: %s" % (self.error_type, self.mesg)

    def dict(self):
        dictinfo = {"error-type": self.error_type,
                    "message": self.mesg}
        return dictinfo

class CommandLineError(Error):
    def __init__(self, mesg, data=None):
        Error.__init__(self,"CMD-Empty-Error", mesg)
        self.data= data

class FormatError(Error):
    def __init__(self, mesg, data=None):
        Error.__init__(self,"JSON-Format-Error", mesg)
        self.data= data

class HandlerError(Error):
    def __init__(self, mesg, data=None):
        Error.__init__(self,"Command-Error", mesg)
        self.data= data

class Status(object):
    def __init__(self, cmd=None):
        self.result = "success"
        self.errors = []

    def append_error(self, err):
        if isinstance(err, Error):
            self.errors.append(err)
            self.result = "fail"
            print self.errors

    def set_success(self):
        self.result = "success"
        self.errors = []

    def set_fail(self):
        self.result = "fail"

    def is_success(self):
        if self.result == "success":
            return True
        else:
            return False

    def is_fail(self):
        if self.result == "fail":
            return True
        else:
            return False

    def dict(self):
        dictinfo = {"result": self.result,
                    "errors": [error.dict() for error in self.errors]}
        return dictinfo
