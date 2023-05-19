_instances = {}
def is_singleton(factory):
    if factory().__class__ in  _instances:
        print('not Singlenton')
    else:
        _instances[factory().__class__] = factory()
        print('is singlenton')

    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not


class MyClass():
    def __init__(self):
        print('initialization...')

    @staticmethod
    def factory():
        return MyClass()

m = MyClass.factory
m1 = MyClass.factory
print(m)

is_singleton(m)
is_singleton(m1)

