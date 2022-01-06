class Sq:

    side = int(input("Enter the length of the side: ")); 

    def length(self):
        print("Side of a Square: ", self.side);


    def area(self):
        print("Area of Square: ", self.side*4);



square1 = Sq();
square1.length();
square1.area();
