from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self, app):
        pass

    def run(self, app):
        self.process(app)

class Laptop(Computer):
    def process(self, app):
        print(f"Laptop is running {app}")

acer = Laptop()
acer.run("Among Us")