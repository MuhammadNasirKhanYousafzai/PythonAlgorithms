from abc import ABCMeta, abstractmethod
class Base():
    __metaclass__=ABCMeta
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass
class Concrete(Base):
    def foo(self):
        pass
c=Concrete()
    # We forget to declare `bar`() again.