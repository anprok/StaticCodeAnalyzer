class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return "Object of the class Patient. name: {name}, last_name: {last_name}, age: {age}".format(
            name=self.name, last_name=self.last_name, age=self.age)

    def __str__(self):
        return "{name} {last_name}. {age}".format(name=self.name, last_name=self.last_name, age=self.age)
