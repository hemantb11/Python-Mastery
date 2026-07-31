from child import c

obj = c()

# Parent class methods
obj.sound()
obj.xyz()

# Child class method
obj.abc()

# Child add() method (Method Overriding)
print("Child Add:", obj.add(10, 20, 30))

# Parent add() method using super()
print("Parent Add:", obj.add_parent(10, 20))