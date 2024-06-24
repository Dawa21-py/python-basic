class person:
    name = "something"
    age = 13
    gender = "male"

    def _init_(self):
        print("persom")


person = person()

print(person.name)


# class House:
#     door = 10
#     window = 5
#     color = "red"

#     def __init__(self, door, window, color):
#         self.door = door 
#         self.window = window
#         self.color = color

# ram_ko_ghar = House(door=2, window=1, color="green")
# print(ram_ko_ghar.color)   
# print(ram_ko_ghar.window)  
# print(ram_ko_ghar.door)    

# shyam_ko_ghar = House(door=3, window=2, color="black")
# print(shyam_ko_ghar.color)   
# print(shyam_ko_ghar.window)  
# print(shyam_ko_ghar.door)    


class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


    def __eq__(self, object):
        return self.age == object.age
    

    def _gt_(self, object):
        return self.salary > object.salary
    
    def _le_(self, object):
        return self.age < object.age


ram = Employee("ram", 25, 3000)
shyam = Employee("shaym", 25, 2500)


print(ram== shyam)