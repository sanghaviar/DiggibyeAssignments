
from datetime import datetime

def time_delta(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    # abs is used to return the positive value
    print(abs(int((t1 - t2).total_seconds())))
    return abs(int((t1 - t2).total_seconds()))


