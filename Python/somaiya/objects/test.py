class cube:
  
  global x;
  x = 0;

  def __init__(self, length=None, breadth=None, height=None, name=None):
      self.length = length; 
      self.breadth = breadth; 
      self.height = height; 

  def namer(self):
      self.name = "Cube " + str(x);
      x = int(x+1);

  def area(self):
    out = self.length * self.breadth * self.height; 
    return out;

cube1 = cube(45, 23, 12);
cube2 = cube(5, 2, 2);

areaOfCube1 = cube1.area()
areaOfCube2 = cube2.area()

cube1.namer()
cube2.namer()

print(cube1.name, ": ", areaOfCube1)
print(cube2.name, ": ", areaOfCube2)
