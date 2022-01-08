# Classes & Objects: 

Classes are template or blueprint to create Objects. With the help of
one class you can create multiple instance of classes also known as
objects. This objects are independent on each other and they also help
in reducing the overall code size of the program.

**EXAMPLE:**

```
class People:
  name = None;

  def create_identity(self, name):
    self.name = name;
    print("Name", name)

person1 = People();
person2 = People();

person1.create_identity("Walter")
person2.create_identity("Aron")

```

## Object Lifecycle: 

There are mainly two thing you need to learn in terms of object lifecycle and they are as follows: 

- Constructor. 
- Destructor. 

### Constructor

Constructors are defined to create classes with attributes.
Whenever, an instance of the object is created the default 
constructor is called i.e `__init__`. 

```
class cube:

  def __init__(self, length=None; breadth=None; height=None):
  if length, breadth, height is None: 
    break;
  else: 
    self.l = length;
    self.b = breadth; 
    self.h = height; 


  def area(self):
    out = l*b*h;
    return out

cube1 = cube();
cube2 = cube();

```










