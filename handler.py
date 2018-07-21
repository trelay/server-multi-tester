import traceback
from errors import *
from subprocess import Popen, PIPE
import shlex
import Queue

Result = Queue.Queue()

def handler(cmd):
    if cmd==None:
        raise CommandLineError("Command is empty")
    args= shlex.split(cmd)
    p= Popen(args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    output = p.communicate()
    return output[0]
    

class Cmd(object):
    def __init__(self,case_name, case_cli):
        self.case_name = case_name
        self.cmd = case_cli
        self.status = Status()
        self.data = None
    def run(self):
        try:
            self.data = handler(self.cmd)
        except Exception, err:
            error = CommandLineError(mesg=str(err))
            self.status.append_error(error)
        results = {"case_name": self.case_name,"case_cli":self.cmd,\
                "response": self.data, "status": self.status.dict()}
        print results
        Result.put(results)

def request_exec(case_name, case_cli):
    Cmd(case_name, case_cli).run()
