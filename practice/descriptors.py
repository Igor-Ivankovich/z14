import pickle


class PickleDescriptor:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        setattr(instance, self.name, pickle.dumps(value))

    def __get__(self, instance, owner):
        if not hasattr(instance, self.name):
            return
        return pickle.loads(getattr(instance, self.name))

    def __delete__(self, instance):
        if hasattr(instance, self.name):
            delattr(instance, self.name)


class MyClass:
    attr = PickleDescriptor('_attr')
    attr1 = PickleDescriptor('_attr1')
    attr2 = PickleDescriptor('_attr2')
