def argsfunc(*args):
    # "args" in *args is variable
    # whatever arguments are supplied are passed as a tuple
    # print(args) == ('arg1','args2','args3',etc...)
    for i in args:
        print(i)

# In [8]: argsfunc('asdf','qwer','zxcv')
# asdf
# qwer
# zxcv

def kwargsfunc(**kwargs):
    # "kwargs" in **kwargs is variable
    # whatever arguments are supplied are passed as a dictionary
    # simple print: kwargsfunc(asdf='qwer', qwer='zxcv') == {'asdf': 'qwer', 'qwer': 'zxcv'}
    for keyword in kwargs:
        print(keyword, kwargs[keyword])

# kwargsfunc(asdf='qwer', qwer='zxcv')
# asdf qwer
# qwer zxcv