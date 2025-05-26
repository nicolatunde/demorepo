# class Line:
#     def __init__(self, coor1, coor2):
#         """
#             Okay, so my method will take in two arguments, both of which are tuples themselves. 
            
#             Each tuple will only contain two items of type int
#         """

#         self.coor1 = coor1
#         self.coor2 = coor2


#     def distance(self):
#         x1 , y1 = self.coor1
#         x2 , y2 = self.coor2
#         formular = ((x2-x1)**2) + ((y2-y1)**2)
#         dist = formular**0.5
#         return dist
    
#     def slope(self):
#         x1 , y1 = self.coor1
#         x2 , y2 = self.coor2
#         lop = (y2 - y1) / (x2 - x1)
#         return lop



# line1 = Line((3,2), (8,10))
# print(line1.distance())
# print(line1.slope())



#  2.	Fill in the class

class Cylinder:
    def __init__(self,height=1, radius=1):
        self.height = height
        self.radius = radius
        self.pi = 22/7
    def volume (self):
        h = self.height
        r = self.radius
        pi = self.pi
        vol = pi*(r**2)*h
        return vol
    def surface_area(self):
        h = self.height
        r = self.radius
        pi = self.pi
        area = 2*pi*r*h+(2*pi*(r**2))
        return area
    


cylinder1 = Cylinder(2,3)
print(cylinder1.volume())
print(cylinder1.surface_area())