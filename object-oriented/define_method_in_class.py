class Person:

    """
        The person class construction method.
        for example:
            p=Person("Alex",22,"China")
            print(p.name,p.age,p.address)

    """
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address


    """
        define the method in person class.
    """
    def greeting(self):
        print("Hello ",self.name)


    def __str__(self):
        return f"Name:{self.name},Age:{self.age},Address:{self.address}"
