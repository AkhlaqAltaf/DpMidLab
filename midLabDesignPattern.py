# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Python Code For Mid Lab Task 
"""
There are Four Classes Required 

1: Students 
2: Computer 
3: Iterator 
4: Teachers  
"""
# Students Class


class Student:
    def __init__(self,name , reg , sem , isAlocated , comp):
        self.stdName=name
        self.stdReg =reg
        self.sem    = sem
        self.isAlocated =isAlocated
        self.comp : comp
    # Computer class 
class Computer:
    def __init__(self , compNo , os , tools , isAlocated , allocatedSTD):
        
        self.compNo  = compNo
        self.os     = os
        self.tools = tools
        self.isAlocated=  isAlocated
        self.alocatedStds = allocatedSTD
    
    
    # Teacher Class For Alocations .........
class Teacher:
     def __init__(self , teacherName , teacherReg):
             
          self.teacherName=teacherName
          self.teacherReg = teacherReg
      
     def alocation(self,stds,comps):
         iterator = Iterator()
        
         stds = iterator.getOddIdStd(stds)
         notAllocatedStds = iterator.getNotAllocatedStds(stds)
         for notAllocated in notAllocatedStds:
             
            
             if comps:
                 
                 computer = comps.popitem()[1]
                 notAllocated.comp = computer
                 notAllocated.isAlocated == True
         
                 
             
          
          
       
        # Iterator class is For Iterating Elements some methods are not using now so i am not implementing
        
class Iterator:
     

     def iterate(self , stds):
         for std in stds:
             self.getStdReg(std)
             

     def getStdReg (self,std):
         return std.stdReg
     
     def getCompId(self,comps):
         pass
         
     
        
     def getOddIdStd(self,stds):
         """
         Here Implementation for Odd integer is Wrong because i have no idea how to implement it 
         """
         odd_stds = []
     
         for std in stds:
             if std.stdReg.__rmod__(2)==0:
                 print("Odd Students",std.stdName)
                 odd_stds.append(std)
             else:
                 
                 print("Even Students",std.stdReg.__rmod__(2))
             
         return odd_stds
     
             
     def isAlocatedStd(self,std):
         if std.isAlocated:
             return False
         else :
             return True
     def isAvailable(self,comp):
         pass
     def getNotAllocatedStds(self,stds):
         not_allocated = []
         for std in stds:
             if self.isAlocatedStd(std) ==False:
                 not_allocated.append(std)
                 
             else :
                 print("Allocated..")
                 
            
         return not_allocated
                 
     

print("Hellow ")        
# There Are Objects Of Students.....................
std1=Student(name="Akhlaq" , reg=1 , sem=6 ,isAlocated=False , comp=None)
std2 = Student("Mudasir", 12, 4, False, None)
std3 = Student("M - Umer", 55, 5, False, None)
# There are List Of students .......................
listofstd = [std1,std2,std3]

# There are Objects Of Computers 


comp1 = Computer(1, "Window", ["Vs Code" , "Jupyter ", "Netbeans"], False, None)
comp2 = Computer(2, "Linux", ["Vs Code" , "Jupyter ", "Netbeans"], False, None)
comp3 = Computer(3, "Window", ["Vs Code" , "Jupyter ", "Netbeans"], False, None)

# Dictionary of computers
dicofcomp = {"Comp1":comp1 , "Comp2":comp2 , "Comp3":comp3}




"""
This is for iterating stds it is for me ...............

print("pop", dicofcomp.popitem()[1].isAlocated)
for item in dicofcomp.values():
    
    print("Item" , item.isAlocated)
    
"""

# Object For Tacher
teacher = Teacher("Mukhtayar Zamin Sahb", 1)
# Computer Allocation To Each Non Allocated Student

teacher.alocation(listofstd , dicofcomp)




   
   
   
   
         
         
    
