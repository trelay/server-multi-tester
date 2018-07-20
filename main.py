#!/usr/bin/env python
from handler import Cmd
import json
import threading

return_json= None

def request_exec(case_name, case_cli, concurrent):
    result = Cmd(case_name, case_cli, concurrent).run()
    print result

def sub_main(requests_str):
    io_thread=[]
    executers= []
    try:
        requests = json.loads(requests_str)['test_cases']
    except:
        raise ValueError("Format is not right")
    for request in requests:
        if request["concurrent"] == True:
            thread=threading.Thread(target=request_exec,kwargs =request)
            io_thread.append(thread)
        else:
            executers.append(request)
    for request in executers:
        request_exec(**request)
    for thread in io_thread:
        thread.start()
        thread.join()

if __name__=="__main__":
    with open("request.json","r") as f:
        requests_str = f.read()
    sub_main(requests_str)
