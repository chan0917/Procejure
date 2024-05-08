
num = 5
dict = {}

def a():
    print('a')
    global dict
    global num
    dict['rk'] = ['eae', 'ee']
    num = 1
    lobby()

def b():
    print('b')
    global num 
    global dict
    dict['rek'] = ['eae', 'ee']
    num = 2
    lobby()

def work(bank_work):
    if bank_work == 1:
        a()
    elif bank_work == 2:
        b()


def lobby():
    print('a, b' , num, dict)
    work(int(input()))


lobby()



