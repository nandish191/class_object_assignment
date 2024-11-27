class Employee_info:
    def __init__(self, name, mob_no, mail_id):
        self.name=name
        self.mob_no=mob_no
        self.mail_id=mail_id

    def validation(self):
        if len(self.mob_no) >10:
            print("not a valid mobile no: ")
        else:
            print("thank you for regn :")
    def email_validatio(self):
        a=(self.mail_id).split('@')
        # print(type(a[0]))
        if type(a[0])==str() or (a[1]=="gmail.com"):
            print("valid mail_id :", self.mail_id)

        else:
            print("not a valid mail_id :")    

    def details(self):
        print(self.name, self.mail_id, self.mob_no)        

obj=Employee_info("raju","9611479302","nandi@gmail.com")
obj.validation()
obj.email_validatio()
obj.details()


class Cuboid:
    def __init__(self, l,b,h):
        self.len=l
        self.bredth=b
        self.height=h
    def area(self):
        return self.len*self.bredth
obj=Cuboid(2,4,6)
print(obj)        
print(obj.area())
obj2=Cuboid(1,2,1)
print(obj2.area())


class Computer:
    def config(self):
        print("8GB RAM 1TB HD i7 Processor ")

hp=Computer()
hp.config()        
dell=Computer()
dell.config()

hp=Computer()
Computer.config(hp)


class Computer:
    def __init__(self):
        self.name="HP"
        self.model=2022

    def config(self):
        print(self.name, self.model) 

obj=Computer()
obj.config()           
obj2=Computer()
obj2.name="Dell"
obj2.config()


class calculation:
    def __init__(self, a, b):
        self.a=a
        self.b=b
        

    def addition(self):
        print( self.a+self.b)
    def multiplication(self):
        print( self.a*self.b)
    def division(self):
        try:
            x=self.a/self.b
            print(x)
        except ZeroDivisionError:
            print("b value should be greter than 0 ")       

obj=calculation(1,0)
obj.addition()
obj.multiplication()
obj.division()


class Values:
    def __init__(self, li=[]):
        self.list=li
    def string_ele(self):
        for ele in self.list:
            if isinstance(ele, str):
                print(ele)
            elif ele%2==0:
                print("even no :", ele) 

            elif isinstance(ele , float):
                print("float no :", ele) 
            elif ele%2!=0:
                print("odd no :", ele )            
    # def even_ele(self):
    #     # for ele2 in self.list:
    #     if ele%2==0:
    #         print("even ele :", ele)            

l=['python', 1,2,33,44,6,8,9,10,"java", "html", 1.2]
obj=Values(l)
obj.string_ele()
# obj.even_ele()

from pydantic import EmailStr
# from datetime import datetime

class Emp_info:
    def __init__(self,id,name, age, email,contct_no):
        self.id=id
        self.name=name
        self.age=age
        self.email=EmailStr
        self.contct_no=contct_no

    def validate(self):
        print(self.contct_no, type(self.contct_no))
        try:
            obj.count(self.contct_no)>1
            print("no already exist")
        except :
            print("successfull")    
        # if self.contct_no.count(self.contct_no)>1:
            
        #     print("no already exist")

        # else:
        #     print("no added successfully")  

    def show_info(self):
        print(self.id, self.name, self.age, self.email,self.contct_no)        

obj=Emp_info(1,"raju",22,'nandu@gmail.com','7411315773') 
# obj.validate()
obj.contct_no='7411315773' 
obj.validate()        
obj.show_info()      
obj=Emp_info(2,"raju",22,'nandu.com','7411315773') 
obj.validate()


class stu_info:
    def __init__(self,id ,name, age,course):
        self.id=id
        self.name=name
        self.age=age
        self.course=course
    
    def validate(self):
        if self.age>30:
            print("not eligible for admission")    
        elif isinstance(self.id, str):
            print("enter valid id ")
        else:
            print("eligible for admission")
    

ob=stu_info(2,'raju',22,"BE")
print(ob)  
print(ob.id)
print(ob.name)
ob.validate()


