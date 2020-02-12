#python programming showing
#use of property( ) function

class Property_fun_demo:
       #def __init__(self):
       #self._age = 0

    def get_age(self):
        #function to get value of  _age
        print("Getter method called")
        return self._age

    def set_age(self,a):
        #function to set value of _age
        print("Setter method called")
        self._age = a

    def del_age(self):
        #function to delete _age attribute
            del self._age
    age=property(get_age,set_age,del_age)


#creating a object of class
mark = Property_fun_demo()
#calling method through object
mark.age = 10
print(mark.age)
