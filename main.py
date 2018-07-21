#!/usr/bin/env python
from handler import request_exec,Result
import json
import threading
from errors import *

def executer(requests):
    io_thread=[]
    executers= []
    for request in requests:
        if request["concurrent"] == True:
            thread=threading.Thread(target=request_exec,\
                   args =(request["case_name"],request["case_cli"]))
            io_thread.append(thread)
        else:
            executers.append(request)
    for request in executers:
        request_exec(request["case_name"],request["case_cli"])
    for thread in io_thread:
        thread.start()
        thread.join()

def main():
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
    '''
    try:
        data = test_cases.append(executer(requests['test_cases']))
    except Exception, err:
        status.append_error(err)
    requests["test_cases"]= Result.get()
    requests["status"]=status.dict()
    print requests
    '''
    Result.get()
    executer(requests['test_cases'])

if __name__=="__main__":
    main()
