class MyClass:

    def method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls
    
    @staticmethod
    def static_method():
        return 'static method'


my_class = MyClass()

print(my_class.method())
print(my_class.class_method())
print(my_class.static_method())
