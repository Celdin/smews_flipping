import sys,os,time

__tests = []

log_file = "test.csv"

def begin(target, what):
    global __tests
    __tests.append({"time": time.strftime("%Y-%m-%d %H:%M:%S"), "target": target, "what": what, "success": False, "why": "Unknow reason"})

def success():
    global __tests
    __tests[len(__tests)-1]["success"] = True
    __tests[len(__tests)-1]["time"] = time.strftime("%Y-%m-%d %H:%M:%S")
    sys.stdout.write(".")
    sys.stdout.flush()

def fail(message=None):
    global __tests
    if message:
        __tests[len(__tests)-1]["why"] = message
    __tests[len(__tests)-1]["time"] = time.strftime("%Y-%m-%d %H:%M:%S")
    sys.stdout.write("X")
    sys.stdout.flush()

def output_report(message, stderr):
    global log_file
    logfile = open(log_file, mode="a+")
    logfile.write(message)
    if stderr:
        sys.stderr.write(message)
    logfile.close()

def report(printfail=False, printsuccess=False):
    global __tests,log_file
    if not len(__tests):
        return
    print("")
    logfile = open(log_file,"w")
    logfile.close()
    success = 0
    for test in __tests:
        if not test["success"]:
            output_report("{};FAIL;{};{};{}\n".format(test["time"],test["target"], test["what"], test["why"]), printfail)
        else:
            output_report("{};SUCCESS;{};{}\n".format(test["time"],test["target"], test["what"]), printsuccess)
            success = success + 1
    print("{}/{} tests passed ({:.2f} %)".format(success, len(__tests), success / len(__tests) * 100))
#####################################################
