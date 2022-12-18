
counter = {}
text = 'Function {} was called {} times.\n'
def call_times(file_name):
    def inner(func):
        def wrapper():
          wrapper.count += 1
          counter[func.__name__] = wrapper.count
          with open(file_name, 'w') as f:
               for func_name, quantity in counter.items():
                  f.write(text.format(func_name, quantity))
          return func()
        wrapper.count = 0
        return wrapper
    return inner

@call_times('foo.txt')
def foo():
    pass

@call_times('foo.txt')
def boo():
    pass

@call_times('calls.txt')
def doo():
    pass

for i in range(5):
    foo()

for i in range(10):
    boo()

dict.clear(counter)

for i in range(15):
    doo()