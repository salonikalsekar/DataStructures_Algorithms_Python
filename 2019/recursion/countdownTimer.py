import time

def recur_countDown(n):
    if n >= 0:
        print(n)
        time.sleep(2)
        recur_countDown(n-1)
    return 0;


def iter_countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1

    print(n)


iter_countdown(5)

recur_countDown(5)