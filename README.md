# PyVector
A python class that implements a Vector, complete with math operations and functions.

# Constructors
The Vector Class has 3 constructors. 
- A series of numbers:
```
v1 = Vector(1.0, 2.0, 3.0)
print(v1) # prints (1.0, 2.0, 3.0)
```
- A list of numbers:
```
l = [1.0, 2.0, 3.0]
v1 = Vector(l)
print(v1) # prints (1.0, 2.0, 3.0)
```
- A tuple of an int and a number. The first element is the number of dimensions and the second is the number that all dimensions will be initialized to:
```
v1 = Vector((3, 1.0))
print(v1) # prints (1.0, 1.0, 1.0)
```
