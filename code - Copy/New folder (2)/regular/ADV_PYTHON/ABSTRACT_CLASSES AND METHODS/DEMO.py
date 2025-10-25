what is non abstract method ?
   >> A method which is having some logic

   def myFun(self):
       print("non abstract method ")
     
what is null body method ?
   >> A method which is not having any logic
   >> null body method acts a non abstract method
   but non abstract method never acts null body mtd.

   def myFun(self):
       pass
    
what is an abstract method ?
    >> an abstract method is a method
    which is not having any logic and it should be
    defined with @abstractmethod

    @abstractmethod
    def myFun(self):
        pass

what is a class ?
   - class is the collection of non abstract method
   
what is an abstract class ?
    - An abstract class is the collection of both abstract
      or non abstract methods

    - Defining the abstract class is nothingbut
    creating the sub class of class ABC [ABstract Class]

    from abc import ABC
    
    class Test(ABC):    #Abstract class 
        pass

    class Test(Exception):   #Exception class
        pass


When do we use abstract methods ?
   - Whenever 2 or more sub classes are required to
   fulfill the same role through different implementation
   
what is a concrete class ?












