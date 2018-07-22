#TODO fix this later

class CommandLineError(Exception):
    pass

class FileNotFountError(Exception):
    pass

class FormatError(Exception):
    pass

class HandlerError(Exception):
    pass

class Status(object):
    def __init__(self, cmd=None):
        self.result = "success"
        self.errors = []

    def append_error(self, err):
        if isinstance(err, Exception):
            self.errors.append(err)
            self.result = "fail"

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
                    "errors": [error for error in self.errors]}
        return dictinfo
