
def my_fun(*args):
    for arg in args:
        print("multiple argument *args : "+ arg)


def my_fun_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("key :" + key + "--- value :"+value)


def my_fun_kwargs(arg1, **kwargs):
    print("arg1 value:" + arg1)
    for key, value in kwargs.items():
        print("key :" + key + "--- value :"+value)


my_fun("hello","world","data_engineer")
#my_fun_kwargs(first='1', mid='mid-cap', last='1001 large-cap')
my_fun_kwargs("argument1", first='1', mid='mid-cap', last='1001 large-cap')


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks111", "arg2": "for111", "arg3": "Geeks111"}
myFun(**kwargs)



