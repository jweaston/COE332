def print_dec(f):
    def func_to_return(*args, **kwargs):
        print("args: {}; kwargs: {}".format(args, kwargs))
        val = f(*args, **kwargs)
        print("return: {}".format(val))
        return val
    return func_to_return

@print_dec
def foo(a):
    return a+1

result = foo(2)
print("Got the result: {}".format(result))