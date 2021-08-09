class Student:
    # Class attributes
    type = 'Student Type'

    def __init__(self, name='Unknown', age=0):
        # Instance attributes.
        self.name = name
        self.__age = age    # Private access attributes.

    def setAge(self, age): self.__age = age

    def getAge(self): return self.__age


# ------- Testcases -------

studentA = Student()
studentB = Student('B', 20)

# Access to Class attributes from Instance or Class
print('Get Type from a certain instance: ' + studentA.type)
print('Get Type from class directly: ' + Student.type)
