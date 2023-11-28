# SUPER()
# -it is bbuiltin  method which is useful to call the super class constructors,variables and methods  from the child class


# imp points about super():
# case1:from child class we are not allowed to access parent class instance variables by using super(),compulasary we shud use self only
# but we can access parent class static variables by using super()
#
# case2:from child class constructor and instance method,we can access parent class constucter,instance method,static method and class method by using super()
#
#case3:from child,class method we cannot access parent class instance methods and constructors by using super() directly(but indirectly possible).but we can access parent class static and class methods
#       In special case we can access them by using this synatx: super(child-class_name,cls).m2(cls)
#
#case4:from child class, static method we cannot access anything by using
#       but in special case we can access static method by using this syntax: super(child-class_name,child-class_name).m3() 