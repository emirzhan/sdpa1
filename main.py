class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None
        return cls._instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

singleton1 = Singleton()
singleton1.set_value("Hello, I'm Singleton 1")

singleton2 = Singleton()
singleton2.set_value("Hello, I'm Singleton 2")

print(singleton1.get_value())
print(singleton2.get_value())
