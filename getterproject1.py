class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    #getter method (/kill)<--joke 
    def get_age(self):
        return self.__age

    #setter methord 
    def set_age(self,age):
        self.__age = age

stud = Student("giorno",13)
#revertiving the getter methord
print("Nmae : ",stud.name,stud.get_age())

#revertiving the setter methord
stud.set_age(15)
print("Nmae : ",stud.name,stud.get_age())
