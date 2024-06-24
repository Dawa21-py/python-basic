class person:

    def __init__(self, name, salary, password) -> None:
        self.name = name  # public
        self._salary = salary  # protected
        self._password = password  # private

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, new_password):
        self._password = new_password

    def get_password(self):
        return self._password
    
    def set_password(self, new_password):
        self._password = new_password

ram = person("ram", 12, "123")
ram.set_password("1234")
print(ram.get_password())  
