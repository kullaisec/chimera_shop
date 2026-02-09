import os

def generate_report(name):
    cmd = "cat reports/" + name
    return os.popen(cmd).read()
