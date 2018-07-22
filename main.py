#!/usr/bin/env python
from handler import request_exec
import json
import threading
from errors import *
import Queue

Result = Queue.Queue()
print Result
def executer(requests):
    io_thread=[]
    executers= []
    for request in requests:
        if request["concurrent"] == True:
            thread=threading.Thread(target=request_exec,\
                   args =(Result,request["case_name"],request["case_cli"]))
            io_thread.append(thread)
        else:
            executers.append(request)
    for request in executers:
        request_exec(Result,request["case_name"],request["case_cli"])
    for thread in io_thread:
        thread.start()
        thread.join()

def main():
    data=[]
    status = Status()
    try:
        with open("request.json","r") as f:
            requests_str = f.read()
    except:
        raise FormatError("The json format is not right")
    try:
        requests = json.loads(requests_str)
    except Exception, err:
        raise err("Format is not right")
    try:
        executer(requests['test_cases'])
    except Exception, err:
        status.append_error(err)
    while not Result.empty():
        data.append(Result.get())
    requests["test_cases"]= data
    requests["status"]=status.dict()
    print requests
    '''
    executer(requests['test_cases'])
    print Result.get()
    '''

if __name__=="__main__":
    main()
