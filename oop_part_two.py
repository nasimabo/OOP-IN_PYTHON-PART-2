########################## del attribute ###########################

'''class Student:
    def __init__(self,name):
        self.name = name

s = Student("Nasim")
print(s.name)
del s.name
print(s.name)'''

############################### PUBLIC ##############################
'''class Student:
    def __init__(self,name):
        self.name = name


s = Student("Nasim")
print(s.name)'''


############################### PRIVATE ##############################


'''class Account:
    def __init__(self,acc,pas):
        self.account = acc
        self.__password = pas

    def reset(self):
        print(self.__password)

        


ac = Account("Nasim145","12345")
print(ac.account)
print(ac.reset())'''

'''class person:
    __name = "nasim"
    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

p1 = person()
print(p1.welcome())'''

################################ INHERITANCE #########################

'''class Car:

    @staticmethod
    def start():
        print("starting the car") 
        
    @staticmethod
    def stop():
        print("stop the car") 


class Toyotacar(Car):
    def __init__(self,name):
        self.name = name


c = Toyotacar("HICHIS")
c2 = Toyotacar("MICTOBUSS")

print(c.name)
print(c2.start())'''

###################### MULTI LEVEL INHERITANCE ######################

'''class Car:
    @staticmethod
    def start():
        print("starting the car") 
        
    @staticmethod
    def stop():
        print("stop the car")


class Toyotacar(Car):
    def __init__(self,degin):
        self.degin = degin

class Foftun(Toyotacar):
    def __init__(self,ty):
        self.ty = ty

ca = Foftun("degil")
print(ca.ty)
print(ca.start())'''


###################### MULTIPOL INHERITANCE ######################


'''class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

mul = C()

print(mul.varA)
print(mul.varB)
print(mul.varC)'''

###################### super method ##################

'''class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("starting the car")

    @staticmethod
    def stop():
        print("stop the car")


class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()

c = ToyotaCar("MICROBUSS","Electronics")
print(c.type)'''

######################### classmethod #############################

'''class Person:
    name = "sakib"

    #def changeName(self,name):
        #self.name = name
        #self.__class__.name = "nasim"

    @classmethod
    def changeName(cls,name):
        cls.name = name
        

s = Person()
s.changeName("nasim")
print(s.name)
print(Person.name)'''

############################### properti method ###################

'''class Student:
    def __init__(self,chem,phy,math):
        
        self.chem = chem
        self.phy = phy
        self.math = math
        self.parcentage = str((self.chem + self.phy + self.math)/3) + "%"

    def clsparcentage(self):
        self.parcentage = str((self.chem + self.phy + self.math)/3) + "%"

s = Student(90,80,70)

print(s.parcentage)

s.phy = 86
print(s.phy)

s.clsparcentage()
print(s.parcentage)'''

'''class Student:
    def __init__(self,che,phy,math):
        self.che = che
        self.phy = phy
        self.math = math

    @property
    def parcentage(self):
        return str((self.che + self.phy + self.math) / 3) + "%"

s = Student(90,80,95)
print(s.parcentage)

s.phy = 70
print(s.parcentage)'''


########################### POLYMORPHISM ###################################

################## POLYMORPHISM: operator and  overloding ################

############### POLYMORPHISM: operator and  Dunder function ###########

########################### POLYMORPHISM: __add__ ###########################

'''class Complex:
    def __init__(self,rel,img):
        self.rel = rel
        self.img = img

    def show_number(self):
        print(self.rel, "i +", self.img, "j")

    def __add__(self,num2):
        newrel = self.rel + num2.rel
        newimg = self.img + num2.img
        return Complex(newrel,newimg)
        

    
        
num = Complex(10,5)

num.show_number()

num2 = Complex(4,6)

num2.show_number()

        
new3 = num + num2
new3.show_number()'''

########################### POLYMORPHISM: __sub__ ###########################


'''class Complex:
    def __init__(self,rel,img):
        self.rel = rel
        self.img = img

    def show_number(self):
        print(self.rel, "i -", self.img, "j")

    def __sub__(self,num2):
        newrel = self.rel - num2.rel
        newimg = self.img - num2.img
        return Complex(newrel,newimg)
        

    
        
num = Complex(10,5)

num.show_number()

num2 = Complex(4,6)

num2.show_number()

        
new3 = num - num2
new3.show_number()'''


########################### POLYMORPHISM: pactices qs ###########################

'''class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return (2*(22/7)*self.radius**2)

    def perimeter(self):
        return (2*(22/7)*self.radius)
    

r = Circle(10)
print(r.Area())
print(r.perimeter())'''


'''class Employee:
    def __init__(self,role,dep,saly):
        self.role = role
        self.dep = dep
        self.saly = saly

    def show_detels(self):
        print("role",self.role)
        print("department",self.dep)
        print("salary",self.saly)

class Enginner(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Enginner","IT","75000")

        
        


em = Enginner("Elon mask",40)

em.show_detels()'''



'''class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2):
        return self.price > ord2.price


ord1 = Order("chips",20)
ord2 = Order("frouts",15)

print(ord1.item)
print(ord1.price)


print(ord2.item)
print(ord2.price)


print(ord1 > ord2)'''










