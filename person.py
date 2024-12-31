#### Class Create
class Person:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone
    
    def display(self):
        print(f"Id : {self.id}"),
        print(f'Name : {self.name}'),
        print(f'Phone : {self.phone}')
    