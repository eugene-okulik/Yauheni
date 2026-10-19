def repeat_me(func):

    def wrapper(*args, count=1, **kwargs):
        return [func(*args, **kwargs) for _ in range(count)]
    return wrapper


@repeat_me
def example(text):
    print(text)

example('print me', count=2)